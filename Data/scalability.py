# libraries
import numpy as np
import matplotlib.pyplot as plt
import extract
import input_conv

dico = extract.dico()

# set width of bars
barWidth = 0.40
plt.rcParams.update({'figure.max_open_warning': 0})
plt.figure(figsize=(18.5, 10.5), dpi=80)
# set heights of bars
autotvm_1  = [dico["autotvm"][1][key]  for key in dico["autotvm"][1]]
autotvm_2  = [dico["autotvm"][2][key]  for key in dico["autotvm"][2]]
autotvm_4  = [dico["autotvm"][4][key]  for key in dico["autotvm"][4]]
autotvm_8  = [dico["autotvm"][8][key]  for key in dico["autotvm"][8]]
autotvm_16 = [dico["autotvm"][16][key] for key in dico["autotvm"][16]]
autotvm_32 = [dico["autotvm"][32][key] for key in dico["autotvm"][32]]

tvm_1 =  [dico["tvmttile"][1][key]  for key in dico["tvmttile"][1]]
tvm_16 = [dico["tvmttile"][16][key]  for key in dico["tvmttile"][16]]
tvm_32 = [dico["tvmttile"][32][key]  for key in dico["tvmttile"][32]]

# Set position of bar on X axis
r1 = np.arange(len(autotvm_1))*4
print(r1)
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]
r8 = [x + barWidth for x in r7]
r9 = [x + barWidth for x in r8]

# Make the plot
plt.bar(r1, autotvm_1, color='#581845', width=barWidth, edgecolor='white', label='autotvm 1')
# plt.bar(r2, autotvm_2, color='#900C3F', width=barWidth, edgecolor='white', label='autotvm 2')
# plt.bar(r3, autotvm_4, color='#C70039', width=barWidth, edgecolor='white', label='autotvm 4')
# plt.bar(r4, autotvm_8, color='#FF5733', width=barWidth, edgecolor='white', label='autotvm 8')
# plt.bar(r5, autotvm_16, color='#FFC300', width=barWidth, edgecolor='white', label='autotvm 16')
# plt.bar(r6, autotvm_32, color='#24FF00', width=barWidth, edgecolor='white', label='autotvm 32')

plt.bar(r7, tvm_1, color='#0000FF', width=barWidth, edgecolor='white', label='tvm+ttile 1')
# plt.bar(r8, tvm_16, color='#008080', width=barWidth, edgecolor='white', label='tvm+ttile 16')
# plt.bar(r9, tvm_32, color='#00FFFF', width=barWidth, edgecolor='white', label='tvm+ttile 32')
plt.yscale("log")
plt.ylabel('Time (ms), log scale', fontweight='bold')
# Add xticks on the middle of the group bars
plt.xlabel('conv', fontweight='bold')
print(len([conv for conv in input_conv.input_conv]))
print(len(autotvm_1))
plt.xticks([4*r + barWidth for r in range(len(autotvm_1))], [conv for conv in input_conv.input_conv], rotation=90)

# Create legend & Show graphic
plt.legend()
plt.savefig("Images/scal.jpg")

# plt.show()
#
# for conv in input_conv.input_conv:
#     # set heights of bars
#     autotvm_1  = [dico["autotvm"][1][conv]  ]
#     autotvm_2  = [dico["autotvm"][2][conv]  ]
#     autotvm_4  = [dico["autotvm"][4][conv]  ]
#     autotvm_8  = [dico["autotvm"][8][conv]  ]
#     autotvm_16 = [dico["autotvm"][16][conv] ]
#     autotvm_32 = [dico["autotvm"][32][conv] ]
#
#     tvm_1 =  [dico["tvmttile"][1][conv]]
#     tvm_16 = [dico["tvmttile"][16][conv]]
#     tvm_32 = [dico["tvmttile"][32][conv]]
#     plt.figure(figsize=(18.5, 10.5), dpi=80)
#
#     l = [autotvm_1[0], autotvm_2[0], autotvm_4[0], autotvm_8[0], autotvm_16[0], autotvm_32[0], tvm_1[0], tvm_16[0], tvm_32[0]]
#     # Set position of bar on X axis
#     r1 = np.arange(len(l))
#
#
#     # Make the plot
#     plt.bar(r1, l, color='#010000', width=barWidth, edgecolor='white', label=conv)
#
#     plt.xlabel('Time (ms), log scale', fontweight='bold')
#     # Add xticks on the middle of the group bars
#     plt.xlabel('conv', fontweight='bold')
#     # print(len([conv for conv in input_conv.input_conv]))
#     # print(len(autotvm_1))
#     plt.xticks([r + barWidth - 0.5 for r in range(len(l))], ["autotvm 1", "autotvm 2", "autotvm 4", "autotvm 8", "autotvm 16", "autotvm 32", "tvm 1", "tvm 16", "tvm 32"], rotation=45)
#     # for index, value in enumerate(l):
#     #     plt.text(value, index, str(value))
#     # Create legend & Show graphic
#     plt.ylabel('Time (ms), log scale', fontweight='bold')
#     plt.legend()
#     plt.savefig(f"Images/scal_{conv}.jpg")
#     plt.clf()
