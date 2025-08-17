def calc_gravitational_lens_angle(M, r):
    G = 6.67430e-11  # 중력 상수
    c = 3e8          # 빛의 속도 (m/s)
    
    alpha = (4 * G * M) / (c**2 * r)  # 휘어짐 각도 (라디안)
    return alpha

def radian_to_degree (M, r):
    angle_degree = calc_gravitational_lens_angle(M, r) * (180 / 3.14)
    return angle_degree

mass = float(input("중력을 형성하는 물체의 질량 : "))
radius = float(input("물체와 최소 접근 거리 : "))

print(radian_to_degree(mass, radius))
