clc; clear all;
opcodes = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0];
opcodes(2) = 90;
opcodes(3) = 74;

counter=0;
current=1;
position = 1;
while current ~= 99
    
    current = opcodes(position);
    
    if current == 1
         if opcodes(position + 1)+1 == 2 | opcodes(position + 1)+1 == 3
             counter =counter +1;
             val = opcodes(opcodes(position + 1)+1) + opcodes(opcodes(position + 2) + 1);
             temp=0
             
         end
         
        
         opcodes(opcodes(position + 3)+1) = opcodes(opcodes(position + 1)+1) + opcodes(opcodes(position + 2) + 1);
    elseif current == 2
        if opcodes(position + 2)+1 == 2 | opcodes(position + 2)+1 == 3
             counter =counter +1;
             val = opcodes(opcodes(position + 1)+1) * opcodes(opcodes(position + 2) + 1);
             temp=0
             
         end
         opcodes(opcodes(position + 3)+1) = opcodes(opcodes(position + 1)+1) * opcodes(opcodes(position + 2) + 1);
    end
    
    position = position +4;
    
    if position > length(opcodes)
        break;
    end
    
    
end