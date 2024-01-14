import React, { FC } from 'react'
import { Text } from '@react-pdf/renderer'
import compose from '../styles/compose'

interface Props {
  className?: string
  placeholder?: string
  value?: string
  onChange?: (value: string) => void
  pdfMode?: boolean
  onFocus?: () => void;  // Add this line
  onBlur?: () => void; 
}

const EditableInput: FC<Props> = ({ className, placeholder, value, onChange, pdfMode, onFocus, onBlur }) => {
  return (
    <>
      {pdfMode ? (
        <Text style={compose('span ' + (className ? className : ''))}>{value}</Text>
      ) : (
        <input
          type="text"
          className={'input ' + (className ? className : '')}
          placeholder={placeholder || ''}
          value={value || ''}
          onChange={onChange ? (e) => onChange(e.target.value) : undefined}
          onFocus={onFocus}  // Add this line
          onBlur={onBlur}
        />
      )}
    </>
  )
}

export default EditableInput
