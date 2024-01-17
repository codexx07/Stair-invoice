import React from 'react';
import { View, Text, Image } from '@react-pdf/renderer';
import logo from './logo.png';

const Footer: React.FC = () => {
    return (
        <View style={style.footer}>
            <Text>Powered By STAIR.</Text>
            <Image src={logo} style={style.image} />
        </View>
    );
}

const style = {
    footer: {
        flexDirection: 'row' as const,
        justifyContent: 'space-between' as const,
        alignItems: 'center' as const,
        padding: 10,
    },
    image: {
        width: 50,
        height: 50,
    },
};

export default Footer;