import React, { FC, useEffect, useState } from 'react'
import { pdf, PDFDownloadLink } from '@react-pdf/renderer'
import { Invoice } from '../data/types'
import InvoicePage from './InvoicePage'

interface Props {
  data: Invoice
  handleFileUpload: () => void
}

const Download: FC<Props> = ({ data, handleFileUpload }) => {
  const [show, setShow] = useState<boolean>(false)

  useEffect(() => {
    setShow(false)

    const timeout = setTimeout(() => {
      setShow(true)
    }, 500)

    return () => clearTimeout(timeout)
  }, [data])

  const sendToServer = async () => {
    const blob = await pdf(<InvoicePage pdfMode={true} data={data} />).toBlob()
    const formData = new FormData()
    formData.append('file', blob, `${data.invoiceTitle ? data.invoiceTitle.toLowerCase() : 'invoice'}_${Date.now()}.pdf`)

    await fetch('http://13.235.18.77:8000/upload-pdf', {
      method: 'POST',
      body: formData
    })

    handleFileUpload()
  }

  return (
    <div className={'download-pdf ' + (!show ? 'loading' : '')} title="Save PDF">
      {show && (
        <button className="server-button" onClick={sendToServer}>
          <PDFDownloadLink
            document={<InvoicePage pdfMode={true} data={data} />}
            fileName={`${data.invoiceTitle ? data.invoiceTitle.toLowerCase() : 'invoice'}_${Date.now()}.pdf`}
            aria-label="Save PDF"
          >
          </PDFDownloadLink>
        </button>
      )}
    </div>
  )
}

export default Download