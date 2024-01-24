import React, { FC, useEffect, useState } from 'react'
import { pdf } from '@react-pdf/renderer'
import { Invoice } from '../data/types'
import InvoicePage from './InvoicePage'

interface Props {
  data: Invoice
}

const Download: FC<Props> = ({ data }) => {
  const [show, setShow] = useState<boolean>(false)

  useEffect(() => {
    setShow(false)

    const timeout = setTimeout(() => {
      setShow(true)
    }, 500)

    return () => clearTimeout(timeout)
  }, [data])

  const handleDownload = async () => {
    const blob = await pdf(<InvoicePage pdfMode={true} data={data} />).toBlob()
    const formData = new FormData()
    formData.append('file', blob, `${data.invoiceTitle ? data.invoiceTitle.toLowerCase() : 'invoice'}.pdf`)
    
    const response = await fetch('http://localhost:3001/upload-pdf', {
      method: 'POST',
      body: formData,
    })

    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
  }

  return (
    <div className={'download-pdf ' + (!show ? 'loading' : '')} title="Save PDF">
      {show && (
        <button onClick={handleDownload} aria-label="Save PDF">
          Download
        </button>
      )}
    </div>
  )
}

export default Download