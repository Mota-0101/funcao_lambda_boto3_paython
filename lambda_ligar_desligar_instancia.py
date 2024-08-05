import json
import boto3

cliente_ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    
    print(event)
    
    instance_id = 'i-0fce81c2be2c83cbe'
    
    ligar = 'projeto1-start' in event['resources'][0]
    desligar = 'projeto1-stop' in event['resources'][0]
    if ligar:
        cliente_ec2.start_instances(InstanceIds=[instance_id])
        mensagem = "Instância inicializada."
    elif desligar:
        cliente_ec2.stop_instances(InstanceIds=[instance_id])
        mensagem = "Instância parada."
    else:
        mensagem = "Nenhuma instância mudou de estado!"
    return {
        'statusCode': 200,
        'body': mensagem
    }
  