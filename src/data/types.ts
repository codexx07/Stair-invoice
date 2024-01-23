import { CSSProperties } from 'react'

export interface ProductLine {
  description: string
  quantity: string
  rate: string
  discount: string
  CGST: string
  SGST: string
  IGST: string
  ISCN: string
  SAC: string
}

export interface Invoice {
  logo: string
  logoWidth: number
  sign: string
  signWidth: number
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
  iscnCode: string
  sacnumber: string

  invoiceTitleLabel: string
  invoiceTitle: string
  invoiceDateLabel: string
  invoiceDate: string
  invoiceDueDateLabel: string
  invoiceDueDate: string
  invoiceieLabel: string


  productLineDescription: string
  productLineQuantity: string
  productLineQuantityRate: string
  productLineQuantityAmount: string
  productLineQuantityDiscount: string
  productLineQuantityCGST: string
  productLineQuantitySGST: string
  productLineQuantityIGST: string
  productLineQuantityISCN: string
  productLineQuantitySAC: string

  productLines: ProductLine[]

  subTotalLabel: string
  taxLabel: string
  advance: string
  advanceamt: string
  dueLabel: string
  ie: string
  ieLabel: string
  due: string


  totalLabel: string
  currency: string

  notesLabel: string
  notes: string
  termLabel: string
  term: string
  footerLabel: string
  footerimage: string
}

export interface CSSClasses {
  [key: string]: CSSProperties
}
