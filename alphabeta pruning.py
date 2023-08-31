 function minimax(node, depth, alpha, beta, maximizingPlayer) is  
if depth ==0 or node is a terminal node then  
return static evaluation of node  
  
if MaximizingPlayer then      
   maxEva= -infinity            
   for each child of node do  
   eva= minimax(child, depth-1, alpha, beta, False)  
  maxEva= max(maxEva, eva)   
  alpha= max(alpha, maxEva)      
   if beta<=alpha  
 break  
 return maxEva  
    
else                         
   minEva= +infinity   
   for each child of node do  
   eva= minimax(child, depth-1, alpha, beta, true)  
   minEva= min(minEva, eva)   
   beta= min(beta, eva)  
    if beta<=alpha  
  break          
 return minEva
