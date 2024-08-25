from minio import Minio
from minio.error import S3Error

def test_minio():
    client = Minio(
        "localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    bucket_name = "testbucket"
    object_name = "test.txt"
    file_content = "Este é um arquivo txt"

    try:
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' criado com sucesso!")
        else:
            print(f"Bucket '{bucket_name} já existe...'")
    
        with open(object_name, "w") as file:
            file.write(file_content)
        
        client.fput_object(bucket_name, object_name, object_name)
        print(f"arquivo '{object_name}' enviado com sucesso")

        client.fget_object(bucket_name, object_name, f"downloaded_{object_name}")
        print(f"Arquivo '{object_name} feito o download com sucesso!")

    except S3Error as e:
        print(f"Erro: '{e}' ")

if __name__ == "__main__":
    test_minio()