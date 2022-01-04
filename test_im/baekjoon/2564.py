'''


경비원 im 대비


분기를 동서남북으로 기준으로 하면 될거 같다. 동근이 기준(동서남북) -> 가게 위치 (동서남북)

그리고 최소값을 구해야 하니깐 두개의 방향으로 가는 것중에 최솟값을 구하면 될듯,,
굳이 두개의 방향으로 갈 필요가 없는것은 가지말자!

일단 입력부터 받자
'''

hor , ver = map(int, input().split())

number_of_shop = int(input())

shop_pos = []
for i in range(number_of_shop):
    shop_row, shop_col = map(int, input().split())
    shop_pos.append([shop_row, shop_col])

# store_loc = [list(map(int, input().split()))for _ in range(n)]

dong_geun_pos = list(map(int, input().split()))


sum_min_distance = 0

if dong_geun_pos[0] == 1:
    for d, l in shop_pos:
        if d == 1:
            sum_min_distance += abs(dong_geun_pos[1] - l)
        elif d == 2:
            left_way = dong_geun_pos[1] + ver + l
            right_way = (hor - dong_geun_pos[1]) + ver + (hor - l)
            sum_min_distance += min(left_way, right_way)
        elif d == 3:
            sum_min_distance += dong_geun_pos[1] + l
        elif d == 4:
            sum_min_distance += (hor - dong_geun_pos[1]) + l


elif dong_geun_pos[0] == 2:
    for d, l in shop_pos:
        if d == 1:
            left_way = dong_geun_pos[1] + ver + l
            right_way = (hor - dong_geun_pos[1]) + ver + (hor - l)
            sum_min_distance += min(left_way, right_way)
        elif d == 2:
            sum_min_distance += abs(dong_geun_pos[1] - l)
        elif d == 3:
            sum_min_distance += dong_geun_pos[1] + (ver - l)
        elif d == 4:
            sum_min_distance += (hor - dong_geun_pos[1]) + (ver - l)
elif dong_geun_pos[0] == 3:
    for d, l in shop_pos:
        if d == 1:
            sum_min_distance += dong_geun_pos[1] + l
        elif d == 2:
            sum_min_distance += (ver - dong_geun_pos[1]) + l
        elif d == 3:
            sum_min_distance += abs(dong_geun_pos[1] - l)
        elif d == 4:
            left_way = dong_geun_pos[1] + hor + l
            right_way = (ver - dong_geun_pos[1]) + hor + (ver - l)
            sum_min_distance += min(left_way, right_way)
else:
    for d, l in shop_pos:
        if d == 1:
            sum_min_distance += dong_geun_pos[1] + (hor - l)
        elif d == 2:
            sum_min_distance += (ver - dong_geun_pos[1]) + (hor - l)
        elif d == 3:
            left_way = (ver - dong_geun_pos[1]) + hor + (ver - l)
            right_way = dong_geun_pos[1] + hor + l
            sum_min_distance += min(left_way, right_way)
        elif d == 4:
            sum_min_distance += abs(dong_geun_pos[1] - l)

print(sum_min_distance)




