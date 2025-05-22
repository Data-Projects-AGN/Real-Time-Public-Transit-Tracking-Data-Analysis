from kafka.admin import KafkaAdminClient

admin = KafkaAdminClient(bootstrap_servers='10.21.168.19:9092')
print(admin.describe_topics(['positions']))