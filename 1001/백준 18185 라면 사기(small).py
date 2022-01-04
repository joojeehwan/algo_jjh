# // 라면공장 (small)
# #include<cstdio>
# #include<algorithm>
# using namespace std;
# int cnt[10005];
# int ans = 0;
# void calc_3(int i, int n)
# {
#     cnt[i] -= n;
#     cnt[i + 1] -= n;
#     cnt[i + 2] -= n;
#     ans += 7 * n;
# }
# void calc_2(int i, int n)
# {
#     cnt[i] -= n;
#     cnt[i + 1] -= n;
#     ans += 5 * n;
# }
# void calc_1(int i, int n)
# {
#     cnt[i] -= n;
#     ans += 3 * n;
# }
#
# int main()
# {
#     int n;
#     scanf("%d", &n);
#     for (int i = 0; i < n; i++)
#         scanf("%d", cnt + i);
#     for (int i = 0; i < n; i++)
#     {
#         if (cnt[i + 1] > cnt[i + 2])
#         {
#             calc_2(i, min(cnt[i], cnt[i + 1] - cnt[i + 2]));
#             calc_3(i, min(cnt[i], min(cnt[i + 1], cnt[i + 2])));
#             calc_1(i, cnt[i]);
#         }
#         else
#         {
#             calc_3(i, min(cnt[i], min(cnt[i + 1], cnt[i + 2])));
#             calc_2(i, min(cnt[i], cnt[i + 1]));
#             calc_1(i, cnt[i]);
#         }
#     }
#     printf("%d", ans);
# }

# c++ 이라서 파이썬으로 바꾸어보자