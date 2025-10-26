#!/usr/bin/env python3
"""Stripe key with XOR encoding"""

# Encoded configuration data
config_enc = [49, 41, 29, 54, 39, 49, 54, 29, 115, 112, 113, 118, 119, 116, 117, 122, 123, 114, 35, 32, 33, 38, 39, 36, 37, 42, 43, 40, 41, 46, 47, 44, 45, 50, 51, 48, 49, 54]

def decode_config(data):
    return bytes([b ^ 0x42 for b in data]).decode()

stripe_key = decode_config(config_enc)
