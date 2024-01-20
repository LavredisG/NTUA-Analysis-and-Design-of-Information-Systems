# load format: [[worker1], [worker2], [worker4], [worker8]]
# worker1: [total_time, rows/s, metrics/s]
small_influx_load = [[42.68, 28661.00, 321640.06], [21.58, 56671.60, 635981.30], [16.29, 75075.51, 842514.07], [16.46, 74325.84, 834101.15]]
medium_influx_load = [[226.39, 32057.62, 359757.69], [129.77, 55928.96, 627647.19], [103.12, 70379.01, 789808.88], [97.02, 74803.45, 839460.89]]
big_influx_load = [[1024.19, 31887.78, 357851.72], [597.80, 54632.05, 613093.03], [458.30, 71261.89, 799716.75], [478.17, 68299.90, 766476.66]]

# query format: [[worker1], [worker2], [worker4]]
# worker1: [wall_clock_time, queries/s, user_time, system_time, cpu_usage%]
# small database
small_sgb_1_1_1              = [[1.53, 656.42, 0.18, 0.09, 18], [0.93, 1089.98, 0.22, 0.06, 30], [0.59, 1697.78, 0.17, 0.08, 42]]
small_sgb_1_1_12             = [[8.04, 124.63, 0.52, 0.12, 7] , [4.79, 209.47, 0.47, 0.14, 12] , [3.39, 296.55, 0.45, 0.10, 16]]
small_sgb_1_8_1              = [[3.12, 320.87, 0.25, 0.10, 11], [1.96, 513.10, 0.20, 0.12, 10] , [1.56, 646.94, 0.22, 0.09, 20]]
small_sgb_5_1_1              = [[3.63, 276.76, 0.30, 0.15, 12], [2.18, 461.80, 0.26, 0.11, 17] , [1.75, 575.68, 0.27, 0.10, 21]]
small_sgb_5_1_12             = [[27.83, 35.96, 0.87, 0.19, 3] , [16.53, 60.57, 0.76, 0.20, 5]  , [12.20, 82.12, 0.74, 0.15, 7]]
small_sgb_5_8_1              = [[10.14, 98.73, 0.43, 0.13, 5] , [6.03, 166.27, 0.37, 0.12, 8]  , [5.32, 188.40, 0.36, 0.12, 9]]
small_cpu_max_all_1          = [[5.28, 189.53, 0.30, 0.14, 8] , [3.21, 312.44, 0.32, 0.10, 13] , [2.05, 491.57, 0.32, 0.07, 19]]
small_cpu_max_all_8          = [[14.19, 70.59, 0.48, 0.09, 4] , [10.15, 98.67, 0.42, 0.08, 5]  , [10.06, 99.59, 0.47, 0.08, 5]]
small_dgb_1                  = [[7.92, 126.38, 0.45, 0.12, 7] , [4.18, 239.61, 0.32, 0.12, 10] , [2.68, 374.27, 0.34, 0.10, 16]]
small_dgb_5                  = [[31.61, 31.65, 0.71, 0.16, 2] , [17.11, 58.50, 0.64, 0.16, 4]  , [9.58, 104.68, 0.62, 0.10, 7]]
small_dgb_all                = [[61.27, 16.33, 0.80, 0.20, 1] , [33.20, 30.14, 0.87, 0.17, 3]  , [18.73, 53.45, 0.78, 0.16, 5]]
small_high_cpu_all           = [[87.04, 11.49, 2.52, 0.30, 3] , [47.43, 21.09, 2.39, 0.36, 5]  , [29.31, 34.15, 2.41, 0.25, 9]]
small_high_cpu_1             = [[9.88, 101.40, 0.59, 0.17, 7] , [5.44, 184.13, 0.57, 0.16, 13] , [3.46, 290.13, 0.54, 0.10, 18]]
small_lastpoint              = [[3.94, 254.52, 0.33, 0.10, 11], [2.24, 448.35, 0.31, 0.08, 17] , [1.66, 605.36, 0.31, 0.06, 22]]
small_groupby_orderby_limit  = [[32.08, 31.21, 0.76, 0.38, 3] , [18.30, 54.71, 0.50, 0.15, 3]  , [16.99, 58.92, 0.52, 0.14, 3]]

# medium database
medium_sgb_1_1_1             = [[1.58, 636.13, 0.24, 0.08, 20], [0.91, 1102.31, 0.18, 0.08, 28], [0.67, 1515.16, 0.19, 0.08, 42]]
medium_sgb_1_1_12            = [[8.24, 121.50, 0.52, 0.11, 7] , [4.55, 220.57, 0.43, 0.10, 11] , [3.20, 313.71, 0.43, 0.12, 17]]
medium_sgb_1_8_1             = [[3.23, 311.05, 0.30, 0.07, 11], [1.93, 520.95, 0.20, 0.10, 16] , [1.50, 668.86, 0.29, 0.07, 24]]
medium_sgb_5_1_1             = [[3.72, 270.36, 0.34, 0.10, 11], [2.26, 444.36, 0.28, 0.10, 17] , [1.55, 648.64, 0.28, 0.08, 23]]
medium_sgb_5_1_12            = [[29.30, 34.15, 0.85, 0.16, 3] , [16.86, 59.39, 0.72, 0.22, 5]  , [11.38, 88.05, 0.76, 0.13, 7]]
medium_sgb_5_8_1             = [[10.50, 95.40, 0.49, 0.10, 5] , [6.27, 159.82, 0.40, 0.08, 7]  , [5.50, 182.77, 0.41, 0.06, 8]]
medium_cpu_max_all_1         = [[5.44, 183.95, 0.35, 0.11, 8] , [3.34, 300.85, 0.30, 0.10, 12] , [2.15, 477.37, 0.25, 0.10, 16]]
medium_cpu_max_all_8         = [[14.76, 67.81, 0.46, 0.12, 3] , [10.86, 92.18, 0.46, 0.12, 5]  , [10.37, 96.61, 0.50, 0.08, 5]]
medium_dgb_1                 = [[8.26, 121.36, 0.40, 0.17, 6] , [4.48, 223.62, 0.34, 0.14, 11] , [2.70, 372.00, 0.34, 0.12, 17]]
medium_dgb_5                 = [[32.20, 31.07, 0.68, 0.14, 2] , [17.26, 58.00, 0.64, 0.12, 4]  , [9.72, 103.16, 0.62, 0.09, 7]]
medium_dgb_all               = [[62.98, 15.88, 0.86, 0.15, 1] , [33.10, 30.24, 0.83, 0.13, 2]  , [18.89, 53.00, 0.80, 0.10, 4]]
medium_high_cpu_all          = [[108.46, 9.22, 3.49, 0.36, 3] , [58.24, 17.18, 3.44, 0.50, 6]  , [36.56, 27.38, 3.38, 0.46, 10]]
medium_high_cpu_1            = [[12.05, 83.10, 0.69, 0.19, 7] , [6.72, 149.17, 0.76, 0.11, 13] , [4.34, 231.67, 0.68, 0.13, 18]]
medium_lastpoint             = [[9.54, 104.93, 0.44, 0.12, 5] , [5.71, 175.51, 0.40, 0.10, 8]  , [3.85, 260.57, 0.42, 0.08, 13]]
medium_groupby_orderby_limit = [[115.42, 8.67, 0.61, 0.11, 0] , [96.08, 10.41, 0.58, 0.12, 0]  , [94.48, 10.59, 0.64, 0.13, 0]]

# big database
big_sgb_1_1_1                = [[1.63, 615.98, 0.20, 0.10, 19], [0.96, 1053.58, 0.22, 0.08, 32], [0.69, 1456.37, 0.21, 0.06, 40]]
big_sgb_1_1_12               = [[8.46, 118.47, 0.57, 0.15, 8] , [4.80, 209.07, 0.45, 0.13, 12] , [3.18, 315.61, 0.42, 0.10, 16]]
big_sgb_1_8_1                = [[3.29, 304.41, 0.27, 0.08, 10], [2.01, 504.58, 0.29, 0.08, 18] , [1.53, 659.46, 0.25, 0.08, 21]]
big_sgb_5_1_1                = [[3.77, 266.08, 0.29, 0.15, 11], [2.16, 465.63, 0.21, 0.13, 16] , [1.66, 611.51, 0.28, 0.07, 21]]
big_sgb_5_1_12               = [[29.44, 34.00, 0.88, 0.14, 3] , [16.82, 59.51, 0.72, 0.18, 5]  , [11.58, 86.57, 0.73, 0.14, 7]]
big_sgb_5_8_1                = [[10.48, 95.55, 0.45, 0.12, 5] , [6.17, 162.57, 0.34, 0.10, 7]  , [5.42, 185.04, 0.33, 0.12, 8]]
big_cpu_max_all_1            = [[5.33, 187.95, 0.32, 0.10, 7] , [3.11, 322.42, 0.24, 0.10, 11] , [2.04, 491.98, 0.27, 0.06, 16]]
big_cpu_max_all_8            = [[14.87, 67.34, 0.45, 0.11, 3] , [10.59, 94.67, 0.34, 0.09, 4]  , [10.58, 94.80, 0.44, 0.12, 5]]
big_dgb_1                    = [[8.04, 124.48, 0.38, 0.13, 6] , [4.36, 230.11, 0.30, 0.11, 9]  , [2.58, 389.30, 0.32, 0.11, 16]]
big_dgb_5                    = [[32.70, 30.60, 0.67, 0.16, 2] , [17.42, 57.45, 0.64, 0.12, 4]  , [9.87, 101.57, 0.60, 0.11, 7]]
big_dgb_all                  = [[63.83, 15.67, 0.87, 0.20, 1] , [33.43, 29.94, 0.79, 0.18, 2]  , [19.30, 51.89, 0.77, 0.15, 4]]
big_high_cpu_all             = [[111.40, 8.98, 3.57, 0.56, 3] , [59.98, 16.68, 3.39, 0.51, 6]  , [37.40, 26.76, 3.42, 0.39, 10]]
big_high_cpu_1               = [[12.03, 83.22, 0.68, 0.16, 7] , [6.58, 152.35, 0.64, 0.12, 11] , [4.05, 248.06, 0.57, 0.13, 17]]
big_lastpoint                = [[29.57, 33.84, 0.57, 0.12, 2] , [17.07, 58.63, 0.52, 0.12, 3]  , [12.03, 83.31, 0.50, 0.11, 5]]
big_groupby_orderby_limit    = [[510.22, 1.96, 0.78, 0.13, 0] , [426.64, 2.34, 0.74, 0.11, 0]  , [423.36, 2.36, 0.79, 0.12, 0]]