protoc -I=./node_modules/protoc-gen-js/bin -I=. helloworld.proto \
--js_out=import_style=commonjs:. \
--grpc-web_out=import_style=commonjs,mode=grpcwebtext:.