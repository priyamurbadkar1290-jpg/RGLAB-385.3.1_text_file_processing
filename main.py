# This variable contains  path for my file
contact_file = 'data/contact.txt'

def add_contact():
   name = input("Enter the contact's name: ")
   phone = input("Enter the contact's phone number: ")

   #Open file as f  and write to it
   # using a - append mode  (to add)
   # opening files  with 'with'  means it  autocloses  file for us at end  of code block
   with open(contact_file, 'a') as f:
       f.write(f'{name}: {phone}\n')
                         
   # print statement to let user  know  task was successful
   print(f'🎉{name} nas been added to your contact!')

def view_contact():
 try:
        with open(contact_file, 'r') as f:
          contacts = f.readlines()

        # If contacts file exists but empty
        if not contacts:
           print('Your contact list is empty')
        else:
           print('🌟 your Contact List 🌟:')

           for contact in contacts:
              print(contact, end='')

# is if file does not exist
 except FileNotFoundError:
       raise FileNotFoundError('Your Contact List is empty')




# DEF = define a  function
# the paren of functions contain passed  in information
def main():
    # While loop will run until condition runs false
    # condition 'True' , so loop will run forever until we say stop 
    while True:
        print('\nContact List Application: ')
        print('1. Add Contact')
        print('2. View Contact')
        print('3. Quit Contact')
        choice = input('Enter your choice: ')

        # If choice 1 add contact, else  if choice 2  - view  contact, elif choice 3 quit
        if choice == '1':
           add_contact()
        elif choice == '2':
           view_contact()
        elif choice == '3':
           print('GoodBye')
           break # break out of while loop
        else: 
           print('Invalid Choice. Please try again')


# To run a function: invoking, executing, running

# This soecific line of code makes sure the function is NOT run upon import
# Only run  upon calling, not run upon  import  within another page 
if __name__ == "__main__":
   try: 
     main()
   except Exception as e:
     print(f"❌ Error: {e}") 