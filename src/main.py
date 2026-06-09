# src/main.py

# 문제 1.
# GPIO 입력 레벨을 상태 문자열로 변환하세요.
def gpio_level_to_state(level):
    if level == 0:
        return "LOW"
    elif level == 1:
        return "HIGH"
    else:
        # 테스트 코드에서 0, 1이 아닌 경우에도 문자열(str)을 기대하므로 처리
        return "INVALID"


# 문제 2.
# UART 송신용 패킷을 생성하세요.
def make_uart_tx_packet(message):
    # 메시지 끝에 \n을 붙이고 bytes로 인코딩
    return (message + "\n").encode('utf-8')


# 문제 3.
# UART 수신 패킷을 파싱하세요.
def parse_uart_rx_packet(packet):
    # bytes를 문자열로 디코딩하고 끝의 \n(공백 포함) 제거
    return packet.decode('utf-8').strip()


# 문제 4.
# I2C 7-bit 주소가 유효한지 확인하세요.
def is_valid_i2c_address(address):
    # 7-bit 주소 범위는 0(0x00)부터 127(0x7F)까지입니다.
    return 0 <= address <= 127


# 문제 5.
# SPI 전송 프레임을 생성하세요.
def make_spi_transfer_frame(command, payload):
    # [명령어, 데이터길이, 데이터1, 데이터2...] 형태의 리스트 생성
    return [command, len(payload)] + payload