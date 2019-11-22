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




#phenotype = { 'Recessive Homozygous':0, 'Recessive Heterozygous':0, "Dominant Homozygous":0, "Dominant Heterozygous":0  } 

phenotype = [ recessive_homozygous, recessive_heterozygous, dominant_homozygous, dominant_heterozygous  ]

def getInput(prompt_text):
        prompt_input = input(prompt_text + " ")
        return prompt_input 


def split(string):
    return tuple([char for char in string])


def zygous_type(child):
    alleles = ""
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
    


    
    


    






parent1 = getInput("Parent 1 Allele: ")
parent2 = getInput("Parent 2 Allele: ")

print(parent1)
print(parent2)

punnett_squares(parent1, parent2)

print(phenotype)