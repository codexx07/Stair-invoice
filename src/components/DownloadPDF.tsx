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

    // Create a URL from the Blob
    const url = URL.createObjectURL(blob)

    // Create a link element with the URL and a download attribute
    const link = document.createElement('a')
    link.href = url
    link.download = `${data.invoiceTitle ? data.invoiceTitle.toLowerCase() : 'invoice'}.pdf`

    // Append the link to the body
    document.body.appendChild(link)

    // Programmatically click the link to start the download
    link.click()

    // Remove the link from the body
    document.body.removeChild(link)
  }

  return (
    <div className={'download-pdf ' + (!show ? 'loading' : '')} title="Save PDF">
      {show && (
        <button className={'server-button'} onClick={handleDownload} aria-label="Save PDF">
        </button>
      )}
    </div>
  )
}

export default Download