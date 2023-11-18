import random
import os
import tkinter
from tkinter import ttk
win=tkinter.Tk()
win.title("Password Book")


#------------------------------------
#MENU
MENU_label=ttk.Label(win,text="MENU")
MENU_label.grid(column=0,row=0)

MENU_label2=ttk.Label(win,text="Please select any of the option below :-")
MENU_label2.grid(column=0,row=1,sticky=tkinter.W)
#Radio
op=tkinter.StringVar()

op1=ttk.Radiobutton(win,text="Generate a Password",value='op1',variable=op)
op1.grid(column=0,row=2,sticky=tkinter.W)

op2=ttk.Radiobutton(win,text="Search a Password",value='op2',variable=op)
op2.grid(column=0,row=3,sticky=tkinter.W)

op3=ttk.Radiobutton(win,text="Change a Password for a site",value='op3',variable=op)
op3.grid(column=0,row=4,sticky=tkinter.W)

op4=ttk.Radiobutton(win,text="Delete a site and password",value='op4',variable=op)
op4.grid(column=0,row=5,sticky=tkinter.W)

op5=ttk.Radiobutton(win,text="Display all sites and passwords and save as text",value='op5',variable=op)
op5.grid(column=0,row=6,sticky=tkinter.W)
#----------------------------------------------------------------------------
#GO button
p_d={}
def action():
    option=op.get()
    if option=="op1":
        p_gen=tkinter.Toplevel(win)
        p_gen.title("Password Generator")
        
        Length_label=ttk.Label(p_gen,text="Enter the Length of your Password : ")
        Length_label.grid(column=0,row=0,sticky=tkinter.W)

        length_entry=ttk.Entry(p_gen,width=3)
        length_entry.grid(column=1,row=0)
        length_entry.focus()

        p_out=ttk.Label(p_gen,text="")
        p_out.grid(column=0,row=1,columnspan=2,sticky=tkinter.W)

        

        def gen():
            l=int(length_entry.get())
                        
            capital_alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            small_alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m'
             ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
            digit=['0','1','2','3','4','5','6','7','8','9']
            symbol=['!','@','#','$','%','^','&','*','(',')','_','\"','\'',':',';','<',',','>','.','?','/']
            p_list =(capital_alpha + small_alpha + digit + symbol)
            
            password=''
            for i in range(l):
                password+=p_list[random.randint(0,len(p_list)-1)]
            p_out.configure(text="The generated strong password is : "+password)
            
            def save():
                length_entry.configure(state="disabled")
                gen_button.configure(state="disabled")
                p_save.destroy()
                site=ttk.Label(p_gen,text="Enter the Name of site for which you want to save this password :")
                site.grid(column=0,row=4,columnspan=10,sticky=tkinter.W)
                
                site_enter=ttk.Entry(p_gen,width=26)
                site_enter.grid(column=6,row=4)
                site_enter.focus()
                
                def f_save():
                    site_d=site_enter.get()
                    p_d[site_d]=password
                    site_save.destroy()
                    site.destroy()
                    site_enter.destroy()
                    p_out.configure(text="")
                    length_entry.configure(state="active")
                    gen_button.configure(state="active")
                    length_entry.delete(0,tkinter.END)
                                        
                site_save=ttk.Button(p_gen,text="DONE",command=f_save)
                site_save.grid(column=5,row=5)

            p_save=ttk.Button(p_gen,text="SAVE",command=save)
            p_save.grid(column=0,row=3)

        gen_button=ttk.Button(p_gen,text="GENERATE",command=gen)
        gen_button.grid(column=1,row=3)  

    elif option=="op2":
        p_search=tkinter.Toplevel(win)
        p_search.title("Password Search")

        search_label=ttk.Label(p_search,text="Enter the Name of the Site : ")
        search_label.grid(column=0,row=0,sticky=tkinter.W)

        site_entry=ttk.Entry(p_search,width=26)
        site_entry.grid(column=1,row=0,columnspan=10)
        site_entry.focus()

        def search():
            search_button.configure(state="disabled")
            site_entry.configure(state="disabled")
            search_result=ttk.Label(p_search,text="")
            search_result.grid(column=0,row=2,sticky=tkinter.W)
            
            site_name=site_entry.get()            

            if site_name in p_d:
                password=p_d[site_name]
                text=tkinter.Text(p_search,height=1,width=len(p_d[site_name]))
                text.grid(column=1,row=2)
                text.insert(tkinter.END,password)
                text.configure(state="disabled")
                search_result.configure(text="Password for \""+site_name+"\" is -->")
                
            else:
                text=tkinter.Text(p_search,height=1,width=0)
                text.grid(column=1,row=2)
                text.destroy()
                search_result.configure(text="Sorry,the site you searched not found...")

            def s_again():
                search_again.destroy()
                search_result.destroy()
                text.destroy()
                search_button.configure(state="active")
                site_entry.configure(state="active")
                site_entry.delete(0,tkinter.END)
                site_entry.focus()

            search_again=ttk.Button(p_search,text="Search Again",command=s_again)
            search_again.grid(column=2,row=2,columnspan=10)
                

        search_button=ttk.Button(p_search,text="Search",command=search)
        search_button.grid(column=1,row=1,columnspan=10)
    
    elif option=="op3":
        new_p=tkinter.Toplevel(win)
        new_p.title("Password Changer")
        
        search_label=ttk.Label(new_p,text="Enter the Name of the Site : ")
        search_label.grid(column=0,row=0,sticky=tkinter.W)
        
        site_entry=ttk.Entry(new_p,width=26)
        site_entry.grid(column=1,row=0)
        site_entry.focus()

        def find():
            search_result=ttk.Label(new_p,text="")
            search_result.grid(column=0,row=2,sticky=tkinter.W,columnspan=10)
            find_button.configure(state="disabled")
            site_entry.configure(state="disabled")
            site_name=site_entry.get()
            f_search_result=ttk.Label(new_p,text="")
            f_search_result.grid(column=0,row=4)
            if site_name in p_d:
                search_result.configure(text="")
                search_result.configure(text="Enter your new Password :  ")
                new_p_entry=ttk.Entry(new_p,width=26,show='*')
                new_p_entry.grid(column=1,row=2)
                new_p_entry.focus()
                def change():
                    p_d[site_name]=new_p_entry.get()
                    p_change.configure(state="disabled")
                    new_p_entry.configure(state="disabled")
                    f_search_result.configure(text="Your changes have been made successfully...")
                    def new_p_again():
                        new_again.destroy()
                        f_search_result.destroy()
                        search_result.destroy()
                        new_p_entry.destroy()
                        p_change.destroy()
                        find_button.configure(state="active")
                        site_entry.configure(state="active")
                        site_entry.delete(0,tkinter.END)
                        site_entry.focus()
                    new_again=ttk.Button(new_p,text="Change Again",command=new_p_again)
                    new_again.grid(column=1,row=4)

                p_change=ttk.Button(new_p,text="change",command=change)
                p_change.grid(column=1,row=3)
                
            else:
                f_search_result.configure(text="The site you searched not found...")
                def new_p_again():
                        new_again.destroy()
                        f_search_result.destroy()
                        find_button.configure(state="active")
                        site_entry.configure(state="active")
                        site_entry.delete(0,tkinter.END)
                        site_entry.focus()
                new_again=ttk.Button(new_p,text="Change Again",command=new_p_again)
                new_again.grid(column=1,row=4)
                       
        find_button=ttk.Button(new_p,text="Find",command=find)
        find_button.grid(column=1,row=1)
    
    elif option=="op4":
        del_p=tkinter.Toplevel(win)
        del_p.title("Deleting Password")

        search_label=ttk.Label(del_p,text="Enter the Name of the Site : ")
        search_label.grid(column=0,row=0,sticky=tkinter.W)
        
        site_entry=ttk.Entry(del_p,width=26)
        site_entry.grid(column=1,row=0)
        site_entry.focus()

        def search():
            site_entry.configure(state="disabled")
            search_button.configure(state="disabled")
            search_result=ttk.Label(del_p,text="")
            search_result.grid(column=0,row=1,sticky=tkinter.W,columnspan=10)
            
            site_name=site_entry.get()
            f_search_result=ttk.Label(del_p,text="")
            f_search_result.grid(column=0,row=3)
            if site_name in p_d:
                search_result.configure(text=site_name+"---->")
                T=tkinter.Text(del_p,height=1,width=len(p_d[site_name]))
                T.grid(column=0,row=1)
                T.insert(tkinter.END,p_d[site_name])
                T.configure(state="disabled")
                def delete_p():
                    del p_d[site_name]
                    del_button.configure(state="disabled")
                    f_search_result.configure(text="Deleted successfully...           ")
                    T.configure(state="normal")
                    T.delete(1.0,tkinter.END)
                    T.configure(state="disabled")
                    def delete_again():
                        del_again.destroy()
                        f_search_result.destroy()
                        search_result.destroy()
                        del_button.destroy()
                        site_entry.configure(state="active")
                        search_button.configure(state="active")
                        site_entry.delete(0,tkinter.END)
                        T.destroy()
                    
                    del_again=ttk.Button(del_p,text="Delete Another",command=delete_again)
                    del_again.grid(column=1,row=3)
                del_button=ttk.Button(del_p,text="Delete",command=delete_p)
                del_button.grid(column=1,row=1)

                
            else:
                f_search_result.configure(text="Sorry,the site you searched not found...")
                def delete_again():
                        del_again.destroy()
                        f_search_result.destroy()
                        site_entry.configure(state="active")
                        search_button.configure(state="active")
                        site_entry.delete(0,tkinter.END)
                    
                del_again=ttk.Button(del_p,text="Delete Another",command=delete_again)
                del_again.grid(column=1,row=3)
                
        search_button=ttk.Button(del_p,text="Search",command=search)
        search_button.grid(column=1,row=1)

    else:
        dis_all=tkinter.Toplevel(win)
        dis_all.title("All Sites and Passwords")
        
        display_label_main=ttk.Label(dis_all,text="Sites                           Passwords")
        display_label_main.grid(column=0,row=0,sticky=tkinter.W)

        r=1
        for s in p_d:
            display_=ttk.Label(dis_all,text="    "+s+"    --------------> "+p_d[s])
            display_.grid(column=0,row=r,sticky=tkinter.W)
            r+=1
        def save_txt():
            saving=tkinter.Toplevel(dis_all)
            saving.title("Save As")
            save_as_label=ttk.Label(saving,text="Enter File Name : ")
            save_as_label.grid(column=0,row=0)
            save_as_entry=ttk.Entry(saving,width=30)
            save_as_entry.grid(column=1,row=0)
            save_as_entry.focus()
            def ok():
                file_name=save_as_entry.get()
                save_as_entry.destroy()
                ok_button.destroy()
                f=open(str(file_name)+".txt","w")
                f.write("Sites                           Passwords\n")
                for s in p_d:
                    f.write(" "+s+" --------------> "+p_d[s]+"\n")
                path=os.path.realpath(f.name)
                f.close()
                save_as_label.configure(text="The File has been successfully saved as \""+str(file_name)+".txt\" at :-")
                path_label=tkinter.Text(saving,height=1,width=len(path))
                path_label.grid(column=0,row=1)                
                path_label.insert(tkinter.END,path)
                path_label.configure(state="disabled")
            ok_button=ttk.Button(saving,text="OK",command=ok)
            ok_button.grid(column=2,row=0)

        txt_save_button=ttk.Button(dis_all,text="Save as file_name.txt",command=save_txt)
        txt_save_button.grid(column=1,row=r+1)
    
go_button=ttk.Button(win,text="GO",command=action)
go_button.grid(column=1,row=7)

win.mainloop()