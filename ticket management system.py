
class Ticket:

    def __init__(self, ticket_id, customer_name, issue):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.issue = issue
        self.__status = "Open"

    def display(self):
        print("\nTicket ID:", self.ticket_id)
        print("Customer Name:", self.customer_name)
        print("Issue:", self.issue)
        print("Status:", self.__status)

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
        
        
class vipticket(Ticket):
    
    def __init__(self,ticket_id,customer_name,issue,priority):
        
        # one method of constuctur getting details from parent class 
        super().__init__(ticket_id,customer_name,issue)
        
        # second method but lengthy method 
        # self.ticket_id = ticket_id
        # self.customer_name = customer_name
        # self.issue = issue
        # self.__status = "Open"
        
        self.priority = priority
        
    def display(self):
        
        # display for first method 
        
        super().display()
        
        # display method for second 
        
        # print("\nTicket ID:", self.ticket_id)
        # print("Customer Name:", self.customer_name)
        # print("Issue:", self.issue)
        # print("Status:", self.__status)
        
        print("priority:",self.priority)
        
def save_tickets():

    with open("tickets.txt", "w") as file:

        for ticket in tickets:

            file.write(
                f"{ticket.ticket_id},"
                f"{ticket.customer_name},"
                f"{ticket.issue},"
                f"{ticket.get_status()}\n"
            )       
    
tickets = []

try:

    with open("tickets.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if len(data) == 4:

                ticket_id = int(data[0])
                customer_name = data[1]
                issue = data[2]
                status = data[3]

                ticket = Ticket(
                    ticket_id,
                    customer_name,
                    issue
                )

                ticket.set_status(status)

                tickets.append(ticket)

except FileNotFoundError:

    print("No previous tickets found.")


while True:
    
    try:

     print("\n----- Ticket Collection System -----")
     print("1. Create Ticket")
     print("2. View All Tickets")
     print("3. Search Ticket")
     print("4. Close Ticket")
     print("5.Delete ticket:")
     print("6.reopen ticket:")
     print("7.update issue:")
     print("8.total tickets:")
     print("9.open tickets:")
     print("10.Closed tickets:")
     print("11.Exit")

     choice = int(input("Enter your choice:"))
    
         
          
     if choice == 1:

          ticket_id = int(input("Enter Ticket ID: "))
          customer_name = input("Enter Customer Name: ")
          issue = input("Enter Issue: ")

          print("1. Normal Ticket")
          print("2. VIP Ticket")

          ticket_type = int(input("Enter Ticket Type: "))

          if ticket_type == 1:

              ticket = Ticket(
                  ticket_id,
                  customer_name,
                  issue
              )

          elif ticket_type == 2:

              priority = input("Enter Priority (High/Medium/Low): ")

              ticket = vipticket(
                  ticket_id,
                  customer_name,
                  issue,
                  priority
              )

          else:
              print("Invalid Ticket Type")
                

          tickets.append(ticket)
          
          save_tickets()
          
          with open("tickets.txt", "a") as file:
           file.write(
                  f"{ticket.ticket_id},"
                  f"{ticket.customer_name},"
                  f"{ticket.issue},"
                  f"{ticket.get_status()}\n"
                       )

          print("Ticket Created Successfully!")

     elif choice == 2:

              if len(tickets) == 0:
                  print("No tickets available")

              else:
                  for ticket in tickets:
                      ticket.display()

     elif choice == 3:
 
              search_id = int(input("Enter Ticket ID to search: "))

              found = False

              for ticket in tickets:
                  if ticket.ticket_id == search_id:
                      ticket.display()
                      found = True
                      break

              if not found:
                  print("Ticket not found.")

     elif choice == 4:

              close_id = int(input("Enter Ticket ID to close: "))

              found = False

              for ticket in tickets:
                  if ticket.ticket_id == close_id:
                      ticket.set_status("Closed")
                      save_tickets()
                      print("Ticket Closed Successfully!")
                      found = True
                      break

              if not found:
                  print("Ticket not found.")


     elif choice == 5:
             
              ticket_id = int(input("enter the ticket id:"))
              
              found = False
              
              for ticket in tickets:
                  if ticket.ticket_id == ticket_id:
                      tickets.remove(ticket)
                      save_tickets()
                      print("Ticket deleted successfully")
                      found = True
                      break
                  
              if not found:
                      print("Ticket not found.")
                      
     elif choice == 6:
              
              ticket_id = int(input("Enter your ticket id:"))
              
              found = False
              
              for ticket in tickets:
                  if ticket.ticket_id == ticket_id:
                      ticket.set_status("open")
                      save_tickets()
                      print("Ticket reopened successfully")
                      found = True
                      break
                  
              if not found:
                      print("Ticket not found")
                      
     elif choice == 7:
              
              ticket_id = int(input("Enter the ticket number:"))
              
              found = False
              
              for ticket in tickets:
                  if ticket.ticket_id == ticket_id:
                    new_issue = input("Enter the new issue:")
                    ticket.issue = new_issue
                    save_tickets()
                    print("issue updated successfully")
                    found = True
                    break
                
              if not found:
                      print("Ticket not found")
                      
     elif choice == 8:
              
              print("total tickets",len(tickets))
              
     elif choice == 9:

      open_tickets = 0

      for ticket in tickets:

        if ticket.get_status().lower() == "open":

            open_tickets += 1

        print("Open Tickets:", open_tickets)
                      
              
     elif choice == 10:
              
              closed_tickets = 0
              
              for ticket in tickets:
                  
                  if ticket.get_status().lower() == "close":
                      
                      closed_tickets += 1
                      
              print("closed tickets:",closed_tickets)
                      
                      
     elif choice == 11:

                 print("Thank You!")
                 print("Visit Again!")
                 break
                        
                           
     else:
                 print("Ticket is invalid")
                 print("Please try again later")
                 print("cheers buddy")
              
        

    except ValueError:
        print("Please enter numbers only!")

    except Exception as e:
        print("Error:", e)
    
     
          
                
        
                
        