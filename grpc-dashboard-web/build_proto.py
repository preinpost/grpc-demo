import subprocess
import platform
import os

from enum import Enum, auto

class OperatingSystem(Enum):
    windows = auto()
    darwin = auto()
    linux = auto()
    unknown = auto()

class Arch(Enum):
    x86_64 = auto()
    amd64 = auto()
    aarch64 = auto()
    unknown = auto()


# 현재 운영 체제를 확인합니다.
system = platform.system().lower()
machine = platform.machine().lower()

plugin_executable_name = None

if system == OperatingSystem.windows.name and (machine == Arch.x86_64.name or machine == Arch.amd64.name):
    plugin_executable_name = 'protoc-gen-grpc-web-1.5.0-windows-x86_64.exe'

elif system == OperatingSystem.darwin.name and machine == Arch.aarch64.name:
    plugin_executable_name = 'protoc-gen-grpc-web-1.5.0-darwin-aarch64'

elif system == OperatingSystem.linux.name:
    pass
    
else:
    print(f"Unknown operating system: {system}")


# 명령어와 인자를 설정합니다.
proto_path = './src/proto'
js_out = './src/generated'
grpc_web_out = './src/generated'
plugin_path = f'./src/proto/bin/{system}/{plugin_executable_name}'
proto_file = 'helloworld.proto'
node_modules_path = './node_modules/protoc-gen-js/bin/'


# generated direction 생성
if not os.path.isdir(js_out):
    os.makedirs(js_out)

# 환경 변수 설정 (protoc-gen-js executable binary PATH 주입)
env = os.environ.copy()
env['PATH'] = node_modules_path + os.pathsep + env['PATH']


# 명령어 문자열을 만듭니다.
command = [
    'protoc',
    f'--proto_path={proto_path}',
    f'--js_out=import_style=commonjs:{js_out}',
    f'--grpc-web_out=import_style=commonjs,mode=grpcwebtext:{grpc_web_out}',
    f'--plugin=protoc-gen-grpc-web={plugin_path}',
    proto_file
]


# 명령어를 실행합니다.
result = subprocess.run(command, env=env, capture_output=True, text=True)


# 실행 결과를 출력합니다.
if (result.returncode == 0):
    print("Generate Done")
else:
    print("Output:", result.stdout)
    print("Error:", result.stderr)