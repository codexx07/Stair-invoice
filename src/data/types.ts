import { CSSProperties } from 'react'

export interface ProductLine {
  description: string
  quantity: string
  rate: string
  discount: string
}

export interface Invoice {
  logo: string
  logoWidth: number
  title: string
  companyName: string
  name: string
  companyAddress: string
  companyAddress2: string
  country: string
  companyCountry: string
  state: string

  billTo: string
  clientName: string
  clientAddress: string
  clientAddress2: string
  clientCountry: string
  msmeRegNumber: string

  invoiceTitleLabel: string
  invoiceTitle: string
  invoiceDateLabel: string
  invoiceDate: string
  invoiceDueDateLabel: string
  invoiceDueDate: string

  productLineDescription: string
  productLineQuantity: string
  productLineQuantityRate: string
  productLineQuantityAmount: string
  productLineQuantityDiscount: string

  productLines: ProductLine[]

  subTotalLabel: string
  taxLabel: string

  totalLabel: string
  currency: string

  notesLabel: string
  notes: string
  termLabel: string
  term: string
}

export interface CSSClasses {
  [key: string]: CSSProperties
}
