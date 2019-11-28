import itertools

recessive_homozygous = {
  "percent": 0,
  "alleles": "",
  "name": "Recessive Homozygous",
  "count": 0
}

recessive_heterozygous = {
  "percent": 0,
  "alleles": "Recessive Heterozygous",
  "name": "",
  "count": 0 
}

dominant_homozygous = {
  "percent": 0,
  "alleles": "",
  "name": "Dominant Homozygous",
  "count": 0 
}


dominant_heterozygous = {
  "percent": 0,
  "alleles": "",
  "name": "Dominant Heterozygous",
  "count": 0
}

parent1_characteristics = {
 "parent_characteristics1": "",
 "allele": ""
}

parent2_characteristics = {
 "parent_characteristics2": "",
 "allele": ""
}

parents_characteristics = [ parent1_characteristics, parent2_characteristics ] 

phenotype = [ recessive_homozygous, recessive_heterozygous, dominant_homozygous, dominant_heterozygous  ]



def getInput(prompt_text):
        prompt_input = input(prompt_text + " ")
        return prompt_input 


def split(string):
    return tuple([char for char in string])


def zygous_type(child):
    alleles = ''.join(child)
    # check if alleles are homozygous
    # convert to lower case for letter match
    if all(x == child[0] for x in child):
     print("All elements in list are equal")
     s = 1

     # check if alleles are dominant homozygous
     if(any(p.isupper() for p in child)):
             print("Dominant homozygous")
             
             s = 3
    else:
        # else alleles are heterozygous
         s = 2
         # check if alleles are dominant heterozygous
         if(any(p.isupper() for p in child)):
             s = 4
             print("Dominant Heterozygous")
             
    

    switcher = {
        1: "Recessive Homozygous",
        2: "Recessive Heterozygous",
        3: "Dominant Homozygous",
        4: "Dominant Heterozygous"
    }
    p_type = switcher.get(s, "Invalid argument")
    #phenotype[p_type] += 1
    for item in phenotype:
     if (item["name"] == p_type):
         item["count"] += 1
         item["alleles"] = alleles
         item["percent"] = 100 / (len(phenotype) / item["count"])
    
    alleles = ''  
 
    
    

def punnett_squares(parent_1, parent_2):
    
    p1 = split(parent_1)
    p2 = split(parent_2)
    parents = p1 + p2
    child = []
    #count alleles for both parents and create punnett square
    for subset in itertools.combinations(parents, 2):
     
      #print(subset)
      child.append(subset)

    
    child.remove(p1)
    child.remove(p2)
        
    for c in child:
     print(c)
     zygous_type(c)
              

    print(child)
    

    
    

def get_input():

 input_correct = False

 while(input_correct == False):
  
  parent1 = getInput("What is Parent 1 Allele: ")
  if(len(parent1) != 2):
   print("Input length incorrect Please enter it again")
   get_input()

  elif(any(char.isdigit() for char in parent1)):
   print("Input cant contain spaces or numbers please try again")
   input_correct = False
   get_input()
  else:
   parent1_c = getInput("What is parent 1 " + parent1 + " Characteristic:")
   for item in parents_characteristics:
     if (item.keys == "parent_characteristics1"):
         item["parent_characteristics1"] = parent1_c
         item["allele"] = parent1
   input_correct = True
  
  
  
  
  parent2 = getInput("What is Parent 2 Allele: ")

  if(len(parent2) != 2):
   print("Input length incorrect Please enter it again")
   get_input()

  elif(any(char.isdigit() for char in parent2)):
   print("Input cant contain spaces or numbers please try again")
   input_correct = False
   get_input()
  else:
   parent2_c = getInput("What is parent 2 " + parent2 + " Characteristic:")
   for item in parents_characteristics:
     if (item.keys == "parent_characteristics2"):
         item["parent_characteristics2"] = parent2_c
         item["allele"] = parent2
   input_correct = True
  
  
  
  



  
 print(parent1)
 print(parent2)

 punnett_squares(parent1, parent2)

 
 display_child(phenotype)



 
 

def display_child(phenotype):

 print(phenotype)

 print(parents_characteristics)





get_input()
 


  


