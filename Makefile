
deploy:
	zip -r CreateThumbnail.zip .
	aws lambda update-function-code --function-name s3_read_write_zip_test  --zip-file fileb://CreateThumbnail.zip --region=us-east-1
