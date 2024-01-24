import React, { FC, useEffect, useState } from 'react'
import { pdf } from '@react-pdf/renderer'
import { Invoice } from '../data/types'
import InvoicePage from './InvoicePage'
import { handleFileUpload } from './InvoicePage'

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
    formData.append('file', blob, `${data.invoiceTitle ? data.invoiceTitle.toLowerCase() : 'invoice'}_${Date.now()}.pdf`)
    
    const response = await fetch('http://localhost:3001/upload-pdf', {
      method: 'POST',
      body: formData
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        // Call handleFileUpload after the POST request is completed
        handleFileUpload();
      })
      .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
      });

    const url = URL.createObjectURL(blob)

    const link = document.createElement('a')
    link.href = url
    link.download = `${data.invoiceTitle ? data.invoiceTitle.toLowerCase() : 'invoice'}_${Date.now()}.pdf`

    document.body.appendChild(link)

    link.click()

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