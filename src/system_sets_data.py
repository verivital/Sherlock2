import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
time_scale = []
time_scale.append(0)
time_scale.append(1)
time_scale.append(2)
time_scale.append(3)
time_scale.append(4)
time_scale.append(5)
time_scale.append(6)
y_0_0 = []
y_0_0.append(0.488000)
y_0_0.append(0.409589)
y_0_0.append(0.224055)
y_0_0.append(0.073714)
y_0_0.append(0.013756)
y_0_0.append(0.000118)
y_0_0.append(-0.004777)
y_0_1 = []
y_0_1.append(0.038000)
y_0_1.append(-0.779887)
y_0_1.append(-0.980476)
y_0_1.append(-0.472075)
y_0_1.append(-0.094616)
y_0_1.append(-0.010513)
y_0_1.append(-0.009275)
y_1_0 = []
y_1_0.append(0.416000)
y_1_0.append(0.333982)
y_1_0.append(0.163447)
y_1_0.append(0.049487)
y_1_0.append(0.008443)
y_1_0.append(-0.001582)
y_1_0.append(-0.005997)
y_1_1 = []
y_1_1.append(-0.034000)
y_1_1.append(-0.851874)
y_1_1.append(-0.776135)
y_1_1.append(-0.319873)
y_1_1.append(-0.058417)
y_1_1.append(-0.011169)
y_1_1.append(-0.004032)
y_2_0 = []
y_2_0.append(0.446000)
y_2_0.append(0.365485)
y_2_0.append(0.187882)
y_2_0.append(0.058580)
y_2_0.append(0.010244)
y_2_0.append(-0.000972)
y_2_0.append(-0.005561)
y_2_1 = []
y_2_1.append(-0.004000)
y_2_1.append(-0.821880)
y_2_1.append(-0.865875)
y_2_1.append(-0.380822)
y_2_1.append(-0.070238)
y_2_1.append(-0.010970)
y_2_1.append(-0.005898)
y_3_0 = []
y_3_0.append(0.410000)
y_3_0.append(0.327682)
y_3_0.append(0.158430)
y_3_0.append(0.047532)
y_3_0.append(0.008017)
y_3_0.append(-0.001734)
y_3_0.append(-0.006103)
y_3_1 = []
y_3_1.append(-0.040000)
y_3_1.append(-0.857873)
y_3_1.append(-0.758659)
y_3_1.append(-0.307305)
y_3_1.append(-0.055754)
y_3_1.append(-0.011171)
y_3_1.append(-0.003590)
y_4_0 = []
y_4_0.append(0.458000)
y_4_0.append(0.378086)
y_4_0.append(0.197851)
y_4_0.append(0.062408)
y_4_0.append(0.011055)
y_4_0.append(-0.000687)
y_4_0.append(-0.005366)
y_4_1 = []
y_4_1.append(0.008000)
y_4_1.append(-0.809882)
y_4_1.append(-0.901196)
y_4_1.append(-0.405760)
y_4_1.append(-0.075381)
y_4_1.append(-0.011017)
y_4_1.append(-0.006702)
y_5_0 = []
y_5_0.append(0.446000)
y_5_0.append(0.365485)
y_5_0.append(0.187882)
y_5_0.append(0.058580)
y_5_0.append(0.010244)
y_5_0.append(-0.000972)
y_5_0.append(-0.005561)
y_5_1 = []
y_5_1.append(-0.004000)
y_5_1.append(-0.821880)
y_5_1.append(-0.865875)
y_5_1.append(-0.380822)
y_5_1.append(-0.070238)
y_5_1.append(-0.010970)
y_5_1.append(-0.005898)
y_6_0 = []
y_6_0.append(0.494000)
y_6_0.append(0.415890)
y_6_0.append(0.229390)
y_6_0.append(0.076085)
y_6_0.append(0.014194)
y_6_0.append(0.000108)
y_6_0.append(-0.004638)
y_6_1 = []
y_6_1.append(0.044000)
y_6_1.append(-0.773888)
y_6_1.append(-0.995873)
y_6_1.append(-0.485619)
y_6_1.append(-0.100257)
y_6_1.append(-0.009351)
y_6_1.append(-0.009786)
y_7_0 = []
y_7_0.append(0.428000)
y_7_0.append(0.346583)
y_7_0.append(0.173299)
y_7_0.append(0.053195)
y_7_0.append(0.009197)
y_7_0.append(-0.001323)
y_7_0.append(-0.005812)
y_7_1 = []
y_7_1.append(-0.022000)
y_7_1.append(-0.839876)
y_7_1.append(-0.811854)
y_7_1.append(-0.344474)
y_7_1.append(-0.063298)
y_7_1.append(-0.011087)
y_7_1.append(-0.004824)
y_8_0 = []
y_8_0.append(0.456000)
y_8_0.append(0.375986)
y_8_0.append(0.196139)
y_8_0.append(0.061683)
y_8_0.append(0.010872)
y_8_0.append(-0.000756)
y_8_0.append(-0.005411)
y_8_1 = []
y_8_1.append(0.006000)
y_8_1.append(-0.811881)
y_8_1.append(-0.895859)
y_8_1.append(-0.401436)
y_8_1.append(-0.074317)
y_8_1.append(-0.010965)
y_8_1.append(-0.006525)
y_9_0 = []
y_9_0.append(0.438000)
y_9_0.append(0.357084)
y_9_0.append(0.181392)
y_9_0.append(0.056180)
y_9_0.append(0.009776)
y_9_0.append(-0.001129)
y_9_0.append(-0.005672)
y_9_1 = []
y_9_1.append(-0.012000)
y_9_1.append(-0.829878)
y_9_1.append(-0.841865)
y_9_1.append(-0.364643)
y_9_1.append(-0.067141)
y_9_1.append(-0.011000)
y_9_1.append(-0.005428)
y_10_0 = []
y_10_0.append(0.414000)
y_10_0.append(0.331882)
y_10_0.append(0.161774)
y_10_0.append(0.048841)
y_10_0.append(0.008305)
y_10_0.append(-0.001631)
y_10_0.append(-0.006032)
y_10_1 = []
y_10_1.append(-0.036000)
y_10_1.append(-0.853874)
y_10_1.append(-0.770247)
y_10_1.append(-0.315687)
y_10_1.append(-0.057545)
y_10_1.append(-0.011173)
y_10_1.append(-0.003888)
y_11_0 = []
y_11_0.append(0.448000)
y_11_0.append(0.367585)
y_11_0.append(0.189533)
y_11_0.append(0.059200)
y_11_0.append(0.010369)
y_11_0.append(-0.000929)
y_11_0.append(-0.005531)
y_11_1 = []
y_11_1.append(-0.002000)
y_11_1.append(-0.819880)
y_11_1.append(-0.871877)
y_11_1.append(-0.384943)
y_11_1.append(-0.071052)
y_11_1.append(-0.010968)
y_11_1.append(-0.006023)
y_12_0 = []
y_12_0.append(0.436000)
y_12_0.append(0.354984)
y_12_0.append(0.180228)
y_12_0.append(0.055906)
y_12_0.append(0.009793)
y_12_0.append(-0.001109)
y_12_0.append(-0.005665)
y_12_1 = []
y_12_1.append(-0.014000)
y_12_1.append(-0.831878)
y_12_1.append(-0.835863)
y_12_1.append(-0.361838)
y_12_1.append(-0.067007)
y_12_1.append(-0.011109)
y_12_1.append(-0.005433)
y_13_0 = []
y_13_0.append(0.408000)
y_13_0.append(0.325581)
y_13_0.append(0.156757)
y_13_0.append(0.046871)
y_13_0.append(0.007869)
y_13_0.append(-0.001788)
y_13_0.append(-0.006140)
y_13_1 = []
y_13_1.append(-0.042000)
y_13_1.append(-0.859873)
y_13_1.append(-0.752939)
y_13_1.append(-0.303109)
y_13_1.append(-0.054840)
y_13_1.append(-0.011165)
y_13_1.append(-0.003437)
y_14_0 = []
y_14_0.append(0.414000)
y_14_0.append(0.331882)
y_14_0.append(0.161774)
y_14_0.append(0.048841)
y_14_0.append(0.008305)
y_14_0.append(-0.001631)
y_14_0.append(-0.006032)
y_14_1 = []
y_14_1.append(-0.036000)
y_14_1.append(-0.853874)
y_14_1.append(-0.770247)
y_14_1.append(-0.315687)
y_14_1.append(-0.057545)
y_14_1.append(-0.011173)
y_14_1.append(-0.003888)
y_15_0 = []
y_15_0.append(0.434000)
y_15_0.append(0.352884)
y_15_0.append(0.178460)
y_15_0.append(0.055203)
y_15_0.append(0.009633)
y_15_0.append(-0.001167)
y_15_0.append(-0.005704)
y_15_1 = []
y_15_1.append(-0.016000)
y_15_1.append(-0.833878)
y_15_1.append(-0.829861)
y_15_1.append(-0.357399)
y_15_1.append(-0.066029)
y_15_1.append(-0.011085)
y_15_1.append(-0.005276)
y_16_0 = []
y_16_0.append(0.474000)
y_16_0.append(0.394888)
y_16_0.append(0.211662)
y_16_0.append(0.068284)
y_16_0.append(0.012551)
y_16_0.append(-0.000130)
y_16_0.append(-0.005008)
y_16_1 = []
y_16_1.append(0.024000)
y_16_1.append(-0.793885)
y_16_1.append(-0.943887)
y_16_1.append(-0.440662)
y_16_1.append(-0.084053)
y_16_1.append(-0.011584)
y_16_1.append(-0.008055)
y_17_0 = []
y_17_0.append(0.420000)
y_17_0.append(0.338182)
y_17_0.append(0.166792)
y_17_0.append(0.050778)
y_17_0.append(0.008720)
y_17_0.append(-0.001484)
y_17_0.append(-0.005929)
y_17_1 = []
y_17_1.append(-0.030000)
y_17_1.append(-0.847875)
y_17_1.append(-0.787910)
y_17_1.append(-0.328245)
y_17_1.append(-0.060161)
y_17_1.append(-0.011162)
y_17_1.append(-0.004320)
y_18_0 = []
y_18_0.append(0.424000)
y_18_0.append(0.342383)
y_18_0.append(0.170100)
y_18_0.append(0.052029)
y_18_0.append(0.008976)
y_18_0.append(-0.001396)
y_18_0.append(-0.005866)
y_18_1 = []
y_18_1.append(-0.026000)
y_18_1.append(-0.843876)
y_18_1.append(-0.799846)
y_18_1.append(-0.336510)
y_18_1.append(-0.061815)
y_18_1.append(-0.011137)
y_18_1.append(-0.004589)
y_19_0 = []
y_19_0.append(0.496000)
y_19_0.append(0.417990)
y_19_0.append(0.231168)
y_19_0.append(0.076875)
y_19_0.append(0.014340)
y_19_0.append(0.000105)
y_19_0.append(-0.004582)
y_19_1 = []
y_19_1.append(0.046000)
y_19_1.append(-0.771889)
y_19_1.append(-1.001006)
y_19_1.append(-0.490134)
y_19_1.append(-0.102137)
y_19_1.append(-0.008996)
y_19_1.append(-0.009941)
y_20_0 = []
y_20_0.append(0.460000)
y_20_0.append(0.380186)
y_20_0.append(0.199563)
y_20_0.append(0.063132)
y_20_0.append(0.011238)
y_20_0.append(-0.000619)
y_20_0.append(-0.005321)
y_20_1 = []
y_20_1.append(0.010000)
y_20_1.append(-0.807882)
y_20_1.append(-0.906532)
y_20_1.append(-0.410084)
y_20_1.append(-0.076445)
y_20_1.append(-0.011078)
y_20_1.append(-0.006873)
y_21_0 = []
y_21_0.append(0.428000)
y_21_0.append(0.346583)
y_21_0.append(0.173299)
y_21_0.append(0.053195)
y_21_0.append(0.009197)
y_21_0.append(-0.001323)
y_21_0.append(-0.005812)
y_21_1 = []
y_21_1.append(-0.022000)
y_21_1.append(-0.839876)
y_21_1.append(-0.811854)
y_21_1.append(-0.344474)
y_21_1.append(-0.063298)
y_21_1.append(-0.011087)
y_21_1.append(-0.004824)
y_22_0 = []
y_22_0.append(0.476000)
y_22_0.append(0.396988)
y_22_0.append(0.213423)
y_22_0.append(0.069043)
y_22_0.append(0.012748)
y_22_0.append(-0.000056)
y_22_0.append(-0.004961)
y_22_1 = []
y_22_1.append(0.026000)
y_22_1.append(-0.791885)
y_22_1.append(-0.949224)
y_22_1.append(-0.445118)
y_22_1.append(-0.085185)
y_22_1.append(-0.011664)
y_22_1.append(-0.008233)
y_23_0 = []
y_23_0.append(0.424000)
y_23_0.append(0.342383)
y_23_0.append(0.170100)
y_23_0.append(0.052029)
y_23_0.append(0.008976)
y_23_0.append(-0.001396)
y_23_0.append(-0.005866)
y_23_1 = []
y_23_1.append(-0.026000)
y_23_1.append(-0.843876)
y_23_1.append(-0.799846)
y_23_1.append(-0.336510)
y_23_1.append(-0.061815)
y_23_1.append(-0.011137)
y_23_1.append(-0.004589)
y_24_0 = []
y_24_0.append(0.438000)
y_24_0.append(0.357084)
y_24_0.append(0.181392)
y_24_0.append(0.056180)
y_24_0.append(0.009776)
y_24_0.append(-0.001129)
y_24_0.append(-0.005672)
y_24_1 = []
y_24_1.append(-0.012000)
y_24_1.append(-0.829878)
y_24_1.append(-0.841865)
y_24_1.append(-0.364643)
y_24_1.append(-0.067141)
y_24_1.append(-0.011000)
y_24_1.append(-0.005428)
y_25_0 = []
y_25_0.append(0.432000)
y_25_0.append(0.350784)
y_25_0.append(0.176498)
y_25_0.append(0.054362)
y_25_0.append(0.009417)
y_25_0.append(-0.001250)
y_25_0.append(-0.005759)
y_25_1 = []
y_25_1.append(-0.018000)
y_25_1.append(-0.835877)
y_25_1.append(-0.823858)
y_25_1.append(-0.352438)
y_25_1.append(-0.064782)
y_25_1.append(-0.011037)
y_25_1.append(-0.005059)
y_26_0 = []
y_26_0.append(0.460000)
y_26_0.append(0.380186)
y_26_0.append(0.199563)
y_26_0.append(0.063132)
y_26_0.append(0.011238)
y_26_0.append(-0.000619)
y_26_0.append(-0.005321)
y_26_1 = []
y_26_1.append(0.010000)
y_26_1.append(-0.807882)
y_26_1.append(-0.906532)
y_26_1.append(-0.410084)
y_26_1.append(-0.076445)
y_26_1.append(-0.011078)
y_26_1.append(-0.006873)
y_27_0 = []
y_27_0.append(0.474000)
y_27_0.append(0.394888)
y_27_0.append(0.211662)
y_27_0.append(0.068284)
y_27_0.append(0.012551)
y_27_0.append(-0.000130)
y_27_0.append(-0.005008)
y_27_1 = []
y_27_1.append(0.024000)
y_27_1.append(-0.793885)
y_27_1.append(-0.943887)
y_27_1.append(-0.440662)
y_27_1.append(-0.084053)
y_27_1.append(-0.011584)
y_27_1.append(-0.008055)
y_28_0 = []
y_28_0.append(0.416000)
y_28_0.append(0.333982)
y_28_0.append(0.163447)
y_28_0.append(0.049487)
y_28_0.append(0.008443)
y_28_0.append(-0.001582)
y_28_0.append(-0.005997)
y_28_1 = []
y_28_1.append(-0.034000)
y_28_1.append(-0.851874)
y_28_1.append(-0.776135)
y_28_1.append(-0.319873)
y_28_1.append(-0.058417)
y_28_1.append(-0.011169)
y_28_1.append(-0.004032)
y_29_0 = []
y_29_0.append(0.480000)
y_29_0.append(0.401188)
y_29_0.append(0.216955)
y_29_0.append(0.070578)
y_29_0.append(0.013151)
y_29_0.append(0.000096)
y_29_0.append(-0.004865)
y_29_1 = []
y_29_1.append(0.030000)
y_29_1.append(-0.787886)
y_29_1.append(-0.959785)
y_29_1.append(-0.454062)
y_29_1.append(-0.087490)
y_29_1.append(-0.011834)
y_29_1.append(-0.008595)
y_30_0 = []
y_30_0.append(0.406000)
y_30_0.append(0.323281)
y_30_0.append(0.154943)
y_30_0.append(0.046152)
y_30_0.append(0.007707)
y_30_0.append(-0.001847)
y_30_0.append(-0.006181)
y_30_1 = []
y_30_1.append(-0.044000)
y_30_1.append(-0.861872)
y_30_1.append(-0.746752)
y_30_1.append(-0.298557)
y_30_1.append(-0.053844)
y_30_1.append(-0.011157)
y_30_1.append(-0.003270)
y_31_0 = []
y_31_0.append(0.406000)
y_31_0.append(0.323281)
y_31_0.append(0.154943)
y_31_0.append(0.046152)
y_31_0.append(0.007707)
y_31_0.append(-0.001847)
y_31_0.append(-0.006181)
y_31_1 = []
y_31_1.append(-0.044000)
y_31_1.append(-0.861872)
y_31_1.append(-0.746752)
y_31_1.append(-0.298557)
y_31_1.append(-0.053844)
y_31_1.append(-0.011157)
y_31_1.append(-0.003270)
y_32_0 = []
y_32_0.append(0.400000)
y_32_0.append(0.316361)
y_32_0.append(0.149486)
y_32_0.append(0.044029)
y_32_0.append(0.007245)
y_32_0.append(-0.002011)
y_32_0.append(-0.006296)
y_32_1 = []
y_32_1.append(-0.050000)
y_32_1.append(-0.867871)
y_32_1.append(-0.727724)
y_32_1.append(-0.284889)
y_32_1.append(-0.050954)
y_32_1.append(-0.011160)
y_32_1.append(-0.002791)
y_33_0 = []
y_33_0.append(0.454000)
y_33_0.append(0.373886)
y_33_0.append(0.194485)
y_33_0.append(0.061059)
y_33_0.append(0.010744)
y_33_0.append(-0.000800)
y_33_0.append(-0.005441)
y_33_1 = []
y_33_1.append(0.004000)
y_33_1.append(-0.813881)
y_33_1.append(-0.889884)
y_33_1.append(-0.397306)
y_33_1.append(-0.073493)
y_33_1.append(-0.010964)
y_33_1.append(-0.006398)
y_34_0 = []
y_34_0.append(0.420000)
y_34_0.append(0.338182)
y_34_0.append(0.166792)
y_34_0.append(0.050778)
y_34_0.append(0.008720)
y_34_0.append(-0.001484)
y_34_0.append(-0.005929)
y_34_1 = []
y_34_1.append(-0.030000)
y_34_1.append(-0.847875)
y_34_1.append(-0.787910)
y_34_1.append(-0.328245)
y_34_1.append(-0.060161)
y_34_1.append(-0.011162)
y_34_1.append(-0.004320)
y_35_0 = []
y_35_0.append(0.458000)
y_35_0.append(0.378086)
y_35_0.append(0.197851)
y_35_0.append(0.062408)
y_35_0.append(0.011055)
y_35_0.append(-0.000687)
y_35_0.append(-0.005366)
y_35_1 = []
y_35_1.append(0.008000)
y_35_1.append(-0.809882)
y_35_1.append(-0.901196)
y_35_1.append(-0.405760)
y_35_1.append(-0.075381)
y_35_1.append(-0.011017)
y_35_1.append(-0.006702)
y_36_0 = []
y_36_0.append(0.404000)
y_36_0.append(0.320974)
y_36_0.append(0.153124)
y_36_0.append(0.045444)
y_36_0.append(0.007553)
y_36_0.append(-0.001902)
y_36_0.append(-0.006219)
y_36_1 = []
y_36_1.append(-0.046000)
y_36_1.append(-0.863872)
y_36_1.append(-0.740410)
y_36_1.append(-0.294001)
y_36_1.append(-0.052881)
y_36_1.append(-0.011158)
y_36_1.append(-0.003110)
y_37_0 = []
y_37_0.append(0.414000)
y_37_0.append(0.331882)
y_37_0.append(0.161774)
y_37_0.append(0.048841)
y_37_0.append(0.008305)
y_37_0.append(-0.001631)
y_37_0.append(-0.006032)
y_37_1 = []
y_37_1.append(-0.036000)
y_37_1.append(-0.853874)
y_37_1.append(-0.770247)
y_37_1.append(-0.315687)
y_37_1.append(-0.057545)
y_37_1.append(-0.011173)
y_37_1.append(-0.003888)
y_38_0 = []
y_38_0.append(0.492000)
y_38_0.append(0.413789)
y_38_0.append(0.227611)
y_38_0.append(0.075295)
y_38_0.append(0.014048)
y_38_0.append(0.000112)
y_38_0.append(-0.004699)
y_38_1 = []
y_38_1.append(0.042000)
y_38_1.append(-0.775888)
y_38_1.append(-0.990741)
y_38_1.append(-0.481104)
y_38_1.append(-0.098377)
y_38_1.append(-0.009738)
y_38_1.append(-0.009616)
y_39_0 = []
y_39_0.append(0.460000)
y_39_0.append(0.380186)
y_39_0.append(0.199563)
y_39_0.append(0.063132)
y_39_0.append(0.011238)
y_39_0.append(-0.000619)
y_39_0.append(-0.005321)
y_39_1 = []
y_39_1.append(0.010000)
y_39_1.append(-0.807882)
y_39_1.append(-0.906532)
y_39_1.append(-0.410084)
y_39_1.append(-0.076445)
y_39_1.append(-0.011078)
y_39_1.append(-0.006873)
y_40_0 = []
y_40_0.append(0.458000)
y_40_0.append(0.378086)
y_40_0.append(0.197851)
y_40_0.append(0.062408)
y_40_0.append(0.011055)
y_40_0.append(-0.000687)
y_40_0.append(-0.005366)
y_40_1 = []
y_40_1.append(0.008000)
y_40_1.append(-0.809882)
y_40_1.append(-0.901196)
y_40_1.append(-0.405760)
y_40_1.append(-0.075381)
y_40_1.append(-0.011017)
y_40_1.append(-0.006702)
y_41_0 = []
y_41_0.append(0.406000)
y_41_0.append(0.323281)
y_41_0.append(0.154943)
y_41_0.append(0.046152)
y_41_0.append(0.007707)
y_41_0.append(-0.001847)
y_41_0.append(-0.006181)
y_41_1 = []
y_41_1.append(-0.044000)
y_41_1.append(-0.861872)
y_41_1.append(-0.746752)
y_41_1.append(-0.298557)
y_41_1.append(-0.053844)
y_41_1.append(-0.011157)
y_41_1.append(-0.003270)
y_42_0 = []
y_42_0.append(0.408000)
y_42_0.append(0.325581)
y_42_0.append(0.156757)
y_42_0.append(0.046871)
y_42_0.append(0.007869)
y_42_0.append(-0.001788)
y_42_0.append(-0.006140)
y_42_1 = []
y_42_1.append(-0.042000)
y_42_1.append(-0.859873)
y_42_1.append(-0.752939)
y_42_1.append(-0.303109)
y_42_1.append(-0.054840)
y_42_1.append(-0.011165)
y_42_1.append(-0.003437)
y_43_0 = []
y_43_0.append(0.494000)
y_43_0.append(0.415890)
y_43_0.append(0.229390)
y_43_0.append(0.076085)
y_43_0.append(0.014194)
y_43_0.append(0.000108)
y_43_0.append(-0.004638)
y_43_1 = []
y_43_1.append(0.044000)
y_43_1.append(-0.773888)
y_43_1.append(-0.995873)
y_43_1.append(-0.485619)
y_43_1.append(-0.100257)
y_43_1.append(-0.009351)
y_43_1.append(-0.009786)
y_44_0 = []
y_44_0.append(0.418000)
y_44_0.append(0.336082)
y_44_0.append(0.165119)
y_44_0.append(0.050132)
y_44_0.append(0.008582)
y_44_0.append(-0.001533)
y_44_0.append(-0.005963)
y_44_1 = []
y_44_1.append(-0.032000)
y_44_1.append(-0.849875)
y_44_1.append(-0.782022)
y_44_1.append(-0.324059)
y_44_1.append(-0.059289)
y_44_1.append(-0.011166)
y_44_1.append(-0.004176)
y_45_0 = []
y_45_0.append(0.428000)
y_45_0.append(0.346583)
y_45_0.append(0.173299)
y_45_0.append(0.053195)
y_45_0.append(0.009197)
y_45_0.append(-0.001323)
y_45_0.append(-0.005812)
y_45_1 = []
y_45_1.append(-0.022000)
y_45_1.append(-0.839876)
y_45_1.append(-0.811854)
y_45_1.append(-0.344474)
y_45_1.append(-0.063298)
y_45_1.append(-0.011087)
y_45_1.append(-0.004824)
y_46_0 = []
y_46_0.append(0.428000)
y_46_0.append(0.346583)
y_46_0.append(0.173299)
y_46_0.append(0.053195)
y_46_0.append(0.009197)
y_46_0.append(-0.001323)
y_46_0.append(-0.005812)
y_46_1 = []
y_46_1.append(-0.022000)
y_46_1.append(-0.839876)
y_46_1.append(-0.811854)
y_46_1.append(-0.344474)
y_46_1.append(-0.063298)
y_46_1.append(-0.011087)
y_46_1.append(-0.004824)
y_47_0 = []
y_47_0.append(0.494000)
y_47_0.append(0.415890)
y_47_0.append(0.229390)
y_47_0.append(0.076085)
y_47_0.append(0.014194)
y_47_0.append(0.000108)
y_47_0.append(-0.004638)
y_47_1 = []
y_47_1.append(0.044000)
y_47_1.append(-0.773888)
y_47_1.append(-0.995873)
y_47_1.append(-0.485619)
y_47_1.append(-0.100257)
y_47_1.append(-0.009351)
y_47_1.append(-0.009786)
y_48_0 = []
y_48_0.append(0.452000)
y_48_0.append(0.371786)
y_48_0.append(0.192834)
y_48_0.append(0.060439)
y_48_0.append(0.010619)
y_48_0.append(-0.000843)
y_48_0.append(-0.005471)
y_48_1 = []
y_48_1.append(0.002000)
y_48_1.append(-0.815881)
y_48_1.append(-0.883882)
y_48_1.append(-0.393185)
y_48_1.append(-0.072679)
y_48_1.append(-0.010965)
y_48_1.append(-0.006273)
y_49_0 = []
y_49_0.append(0.456000)
y_49_0.append(0.375986)
y_49_0.append(0.196139)
y_49_0.append(0.061683)
y_49_0.append(0.010872)
y_49_0.append(-0.000756)
y_49_0.append(-0.005411)
y_49_1 = []
y_49_1.append(0.006000)
y_49_1.append(-0.811881)
y_49_1.append(-0.895859)
y_49_1.append(-0.401436)
y_49_1.append(-0.074317)
y_49_1.append(-0.010965)
y_49_1.append(-0.006525)
y_upper_0 = []
y_upper_0.append(0.500000)
y_upper_0.append(0.422190)
y_upper_0.append(0.234796)
y_upper_0.append(0.096422)
y_upper_0.append(0.039749)
y_upper_0.append(0.020000)
y_upper_0.append(0.020000)
y_upper_1 = []
y_upper_1.append(0.050000)
y_upper_1.append(-0.767883)
y_upper_1.append(-0.730613)
y_upper_1.append(-0.273910)
y_upper_1.append(0.032487)
y_upper_1.append(0.027430)
y_upper_1.append(0.020000)
y_lower_0 = []
y_lower_0.append(0.400000)
y_lower_0.append(0.316361)
y_lower_0.append(0.149486)
y_lower_0.append(0.026130)
y_lower_0.append(-0.020000)
y_lower_0.append(-0.020000)
y_lower_0.append(-0.020000)
y_lower_1 = []
y_lower_1.append(-0.050000)
y_lower_1.append(-0.867878)
y_lower_1.append(-1.008185)
y_lower_1.append(-0.510344)
y_lower_1.append(-0.167200)
y_lower_1.append(-0.020000)
y_lower_1.append(-0.020000)
fig, (ax_0,ax_1) = plt.subplots( 2 , 1 , sharex = True)
ax_0.plot(time_scale, y_0_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_1_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_2_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_3_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_4_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_5_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_6_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_7_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_8_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_9_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_10_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_11_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_12_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_13_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_14_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_15_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_16_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_17_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_18_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_19_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_20_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_21_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_22_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_23_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_24_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_25_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_26_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_27_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_28_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_29_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_30_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_31_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_32_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_33_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_34_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_35_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_36_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_37_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_38_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_39_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_40_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_41_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_42_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_43_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_44_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_45_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_46_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_47_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_48_0 , color =  'black'  ) 
ax_0.plot(time_scale, y_49_0 , color =  'black'  ) 
ax_0.fill_between(time_scale, y_lower_0, y_upper_0 , color =  'cyan'  ) 
ax_0.set_ylabel( ' $ x_0 $ ' , family =  'serif'   , fontsize = 10 + 10 )
ax_0.set_xlabel('Time Steps' , family =  'serif'  , fontsize = 10)
ax_0.yaxis.set_major_locator(MaxNLocator(4))
ax_1.plot(time_scale, y_0_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_1_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_2_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_3_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_4_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_5_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_6_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_7_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_8_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_9_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_10_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_11_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_12_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_13_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_14_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_15_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_16_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_17_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_18_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_19_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_20_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_21_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_22_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_23_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_24_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_25_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_26_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_27_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_28_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_29_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_30_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_31_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_32_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_33_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_34_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_35_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_36_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_37_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_38_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_39_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_40_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_41_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_42_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_43_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_44_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_45_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_46_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_47_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_48_1 , color =  'black'  ) 
ax_1.plot(time_scale, y_49_1 , color =  'black'  ) 
ax_1.fill_between(time_scale, y_lower_1, y_upper_1 , color =  'cyan'  ) 
ax_1.set_ylabel( ' $ x_1 $ ' , family =  'serif'   , fontsize = 10 + 10 )
ax_1.set_xlabel('Time Steps' , family =  'serif'  , fontsize = 10)
ax_1.yaxis.set_major_locator(MaxNLocator(4))
plt.savefig(  'Sherlock_System_Traces' )
