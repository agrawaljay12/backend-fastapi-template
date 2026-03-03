def send_otp_html(otp):
    return f"""
    <html>
        <body>
            <h2>Your OTP Code</h2>
            <p>Your OTP code is: <strong>{otp}</strong></p>
            <p>This code will expire in 5 minutes.</p>
        </body>
    </html>
    """