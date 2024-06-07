import boto3

# Constantes de E-mail
SENDER_EMAIL = "your-verified-email@example.com"
RECIPIENT_EMAIL = "robertoalbuquerque1509@gmail.com"

def lambda_handler(event, context):
    ses_client = boto3.client('ses', region_name='us-east-1')

    subject = "E-mail de teste do AWS Lambda"
    body_text = "Este é um e-mail de teste enviado de uma função AWS Lambda."
    body_html = """<html>
<head></head>
<body>
  <h1>E-mail de teste do AWS Lambda</h1>
  <p>Este é um e-mail de teste enviado de uma função AWS Lambda.</p>
</body>
</html>"""

    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [RECIPIENT_EMAIL],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': subject,
                },
            },
            Source=SENDER_EMAIL,
        )
        return {
            'statusCode': 200,
            'body': 'Email sent!'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
