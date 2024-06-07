# aws-lambda-ses-email
Envio de email.

# AWS Lambda Function to Send Email using Amazon SES

## Descrição
Esta função AWS Lambda envia um e-mail usando o Amazon Simple Email Service (SES). A função é escrita em Python e utiliza a biblioteca `boto3` para interagir com o SES.

## Entrada Esperada
A função não requer entrada específica para o envio de um e-mail fixo. Para enviar e-mails dinâmicos, você pode ajustar o código para aceitar parâmetros no evento JSON.

## Saída Esperada
A função retorna um status code 200 se o e-mail for enviado com sucesso, ou 500 se houver um erro.

## Dependências Externas
- `boto3`: A biblioteca oficial da AWS para Python.

## Instruções para Execução
1. **Verifique os Endereços de E-mail no SES**:
   - Verifique o endereço de e-mail do remetente e do destinatário no Amazon SES.
2. **Criar a Função Lambda**:
   - Crie uma nova função Lambda no console AWS.
   - Adicione o código fonte contido no arquivo `lambda_function.py`.
   - Configure as permissões da função para permitir o envio de e-mails usando SES.
3. **Testar a Função Lambda**:
   - Use o console do AWS Lambda para configurar um evento de teste com um payload JSON simples `{}`.

## Testando e Depurando
- **Logs do CloudWatch**:
  - A função Lambda registra logs no Amazon CloudWatch. Verifique os logs para depurar problemas.
- **Eventos de Teste**:
  - Configure eventos de teste no console do Lambda para simular diferentes entradas e validar o comportamento da função.

## Exemplo de Evento de Teste
Para enviar um e-mail dinâmico, você pode usar o seguinte evento de teste:

```json
{
  "recipient_email": "viniciuscamacho12@gmail.com",
  "subject": "Test Email from AWS Lambda",
  "body_text": "This is a test email sent from an AWS Lambda function.",
  "body_html": "<html><head></head><body><h1>Test Email from AWS Lambda</h1><p>This is a test email sent from an AWS Lambda function.</p></body></html>"
}
