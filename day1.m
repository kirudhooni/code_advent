clc; clear all;
data = [103910
133712
82560
91679
98354
89007
93288
132363
91373
83666
55958
90387
100869
98127
120197
86931
60370
143999
71541
115662
51287
81624
58307
60408
141664
89781
127772
132353
101220
104001
140488
58072
75764
120003
82386
77603
130604
86672
120987
80334
67674
52918
98041
102541
97612
50436
129998
84854
101867
82039
108966
80708
54588
86854
89607
71869
126093
89460
86558
77651
53295
132188
137266
97370
114620
86691
147199
147299
72616
142654
88610
104030
64256
54867
76532
145081
102335
72987
72684
148155
59739
85954
141001
125171
107764
141622
89536
92435
69038
84518
119700
119801
81677
125317
72683
128905
93666
75633
117361
82295];
final_result=0;
result =0;
for i=1:length(data)
    res = floor(data(i)/3)-2;
    
    result=res;
    new_result=0;
    while (result >0)
    
    mass =floor(result/3)-2;
    if mass<0
        mass =0;
    end
    new_result = new_result+mass;
    result = mass;
        if result<0
            new_result = new_result +2;
        end
    end
    
    final_result = res +final_result+new_result;
end

%     old = result;
%     
%     new_result=0;
% while (result >0)
%     
%     mass =floor(result/3)-2;
%     new_result = new_result+mass;
%     result = mass;
%     if result<0
%         new_result = new_result +2;
%     end
% end
%     final = new_result + old
%     