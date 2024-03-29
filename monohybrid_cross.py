""" Punnet Square generator with Offsping output, this script with take to parents genotypes
    and output the percentage chance of allele expresson. 
    Copyleft (Copyleft) 2019  John Thompson

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>. """

import itertools
from random import randrange

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

off_spring_amount = 0   

# list array of phenotypes 
phenotype = [ recessive_homozygous, recessive_heterozygous, dominant_homozygous, dominant_heterozygous  ]


# get input from command line and return a string
def get_prompt_input(prompt_text):
        prompt_input = input(prompt_text + " ")
        return prompt_input 


# break the into a each character and return a tuple for each genotype
def split(string):
    return tuple([char for char in string])


def zygous_type(child):
    alleles = ''.join(child)
    # check if alleles are homozygous
    
    if all(allele == child[0] for allele in child):
     print("Recessive Homozygous")
     s = 1

     # check if alleles are dominant homozygous
     if(any(allele.isupper() for allele in child)):
             print("Dominant homozygous")
             
             s = 3
    else:
        # else alleles are heterozygous
         s = 2
         print("Recessive Heterozygous")
         # check if alleles are dominant heterozygous
         if(any(allele.isupper() for allele in child)):
             s = 4
             print("Dominant Heterozygous")
             
    

    switcher = {
        1: "Recessive Homozygous",
        2: "Recessive Heterozygous",
        3: "Dominant Homozygous",
        4: "Dominant Heterozygous"
    }
    p_type = switcher.get(s, "Invalid argument")
    
    # iderate though each allele in phenotype and if the switcher matchs the name add a count for each zygous type.
    for item in phenotype:
     if (item["name"] == p_type):
         item["count"] += 1
         item["alleles"] = alleles
         item["percent"] = 100 / (len(phenotype) / item["count"])
    
    alleles = ''  
 
    
    

def punnett_squares(parent_1, parent_2):
    
    # split parent alleles return tuple of characters for each allele 
    p1 = split(parent_1)
    
    p2 = split(parent_2)
    
    # add parents together to create a tuple
    parents = p1 + p2
    
    # create empty child list array
    child = []
    
    # use itertools library to create child combinations alleles from both parents 
    for subset in itertools.combinations(parents, 2):
     
      # append the parent alleles to a list array
      child.append(subset)

    # remove parents alleles from combinations of alleles in the child list
    child.remove(p1)
    child.remove(p2)
        
    for c in child:
     

     # call zygous_type function for each allele in the child list array count and check type
     # each allele is then added to phenotype list of dictionary's  
     zygous_type(c)
              

    print(child)
    


    

def get_input():

 input_correct = False

 while(input_correct == False):
  
  # get command line input
  parent1 = get_prompt_input("What is Parent 1 genotype: ")
  
  # check if the command line input is equal to two characters 
  if(len(parent1) != 2):
   print("Input length incorrect Please enter it again")
   get_input()
  # check if the command line input doesn't contain spaces 
  elif(any(char.isdigit() for char in parent1)):
   print("Input cant contain spaces or numbers please try again")
   input_correct = False
   get_input()
  else:
   input_correct = True
  
  
  
   # get command line input
  parent2 = get_prompt_input("What is Parent 2 genotype: ")
  
  # check if the command line input is equal to two characters
  if(len(parent2) != 2):
   print("Input length incorrect Please enter it again")
   get_input()

  # check if the command line input doesn't contain spaces
  elif(any(char.isdigit() for char in parent2)):
   print("Input cant contain spaces or numbers please try again")
   input_correct = False
   get_input()
  else:
   input_correct = True
   global off_spring_amount 
   
   try:
    off_spring_amount = int(get_prompt_input("How many offspring: "))

   except:
    print("Input must be a interger only")
    get_input()

 punnett_squares(parent1, parent2)

 # call function to display child alleles (punnet square) and statists 
 display_child(phenotype)



 
 

def display_child(phenotype):

 # create blank array list
 alleles_list = []

 # create black dictionary 
 off_spring_dict = {}

 # iterate the phenotype list array of dictionary's
 for p in phenotype:
   # if no count has been added to phenotype list of dictionary's skip printing empty dictionary  
  if(p['count'] != 0):
     print(p['alleles'], " is ", p['name'], "with a ", p['percent'], " percent chance ", )
     print('\n')
     alleles_list.append(p['alleles'])
     
 # iterate for total amount off spring input and randomly choose the a genotype from the alleles list 
 for x in range(0, off_spring_amount):
  i = randrange(len(alleles_list))

 # check if the off_spring_dict contains the genotype and add to the count or create a new entry
  if(any(o == alleles_list[i] for o in off_spring_dict)):
   off_spring_dict[alleles_list[i]] += 1
  else:
   off_spring_dict.update({ alleles_list[i] : 1 })

 print("out of a random selection of ",off_spring_amount, "off spring")

 # print out the contents of the off_spring_dict
 for x in range(0,len(off_spring_dict)):
  key = list(off_spring_dict)[x]
  val = list(off_spring_dict.values())[x]
  print('\n')
  print(key, " alleles ", "would be ", val)





#start program 

get_input()
 


  


