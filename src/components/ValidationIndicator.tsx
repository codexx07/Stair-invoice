// ValidationIndicator.js
import React from 'react';
import { Text, View, StyleSheet } from '@react-pdf/renderer';

const styles = StyleSheet.create({
    valid: {
        textAlign: 'center',
        color: 'green',
    },
    invalid: {
        textAlign: 'center',
        color: 'red',
    },
});

const ValidationIndicator = ({ isValid, isFocused, pdfMode }: { isValid: boolean, isFocused: boolean, pdfMode: boolean }) => {
    if (!isFocused) {
        return null;
    }

    if (pdfMode) {
        return (
            <View style={isValid ? styles.valid : styles.invalid}>
                <Text>{isValid ? '\u2713' : '\u2717'}</Text>
            </View>
        );
    }

    return (
        <div style={{ 
            color: isValid ? 'green' : 'red', 
            backgroundColor: isValid ? '#DFF2BF' : '#FFD2D2', 
            borderRadius: '50%', 
            width: '20px', 
            height: '20px', 
            display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center',
            padding: '5px',
        }}>
            {isValid ? '\u2713' : '\u2717'}
        </div>
    );
};

export default ValidationIndicator;