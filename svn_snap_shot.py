import os,re
##reamde run as python3 svn_snap_shot.py <PATH_NAME>
class dir:
    def __init__(self, name, abs_path):
        print('init called')
        self.name = name
        self.abs_path = abs_path
        self.loan=0
        self.leas=0
        self.line=0
        self.bj=0
        self.cl=0
        self.el=0
        self.ew=0
        self.ex=0
        self.em=0
        self.en=0
        self.jw=0
        self.jsp=0
        self.fc=0
        self.dc=0

    def construct_path(self,con_abs_path):
        con_file_dir_list=os.listdir(path=con_abs_path)
        for con_name in con_file_dir_list:
            self.classify_file(con_name)





    
    def do_something(self):
        print('in display')
        print("Name-", self.name)
        print("Absolute Path", self.abs_path)
        ###
        pks_pattern="[0-9a-z,_]+.pks"
        sql_pattern="[0-9a-z,_]+.sql"
        ###
        bj_pattern="[0-9a-z,_]+_bj_[0-9a-z,_]+.pkb"
        cl_pattern="[0-9a-z,_]+_cl_[0-9a-z,_]+.pkb"
        el_pattern="[0-9a-z,_]+_el_[0-9a-z,_]+.pkb"
        ew_pattern="[0-9a-z,_]+_ew_[0-9a-z,_]+.pkb"
        ex_pattern="[0-9a-z,_]+_ex_[0-9a-z,_]+.pkb"
        em_pattern="[0-9a-z,_]+_em_[0-9a-z,_]+.pkb"
        en_pattern="[0-9a-z,_]+_en_[0-9a-z,_]+.pkb"
        jw_pattern="[0-9a-z,_]+_jw_[0-9a-z,_]+.pkb"
        jsp_pattern="[0-9a-z,_]+.jsp"
        ###
        d_path=self.abs_path
        file_dir_list=os.listdir(path=self.abs_path)
        for name in file_dir_list:
            if (os.path.isdir(os.path.join(d_path, name))):
                self.dc=self.dc+1
                #print(os.path.join(d_path, name))
                if (name=='loan'):
                    self.loan=1
                    #print("loan folder is present")
                    self.construct_path(os.path.join(d_path, name))
                elif (name=='lease'):
                    self.lease=1
                    #print("Lease folder is present")
                    self.construct_path(os.path.join(d_path, name))
                elif (name=='line'):
                    self.line=1
                    #print("Line folder is present")
                    self.construct_path(os.path.join(d_path, name))
                else:
                    #print("Creating a new object")
                    sub_dir=dir(name,os.path.join(d_path, name))
                    sub_dir.do_something()

            elif (os.path.isfile(os.path.join(d_path, name))):
                self.fc=self.fc+1
                #print(os.path.join(d_path, name))
                if re.search(pks_pattern,name):
                    #print("pks found a match")
                    pass
                elif re.search(sql_pattern,name):
                    #print("sql found a match")
                    pass 
                else:
                    self.classify_file(name)
        print('*'*10)
        print("Name is ",self.name)
        print("directory count is ",self.dc)
        print("file count is ",self.fc)
        print("Loan Ind",self.loan)
        print("Lease Ind ",self.leas)
        print("line Ind ",self.line)
        print("BJ",self.bj)
        print("CL",self.cl)        
        print("EL",self.el)
        print("EW",self.ew)
        print("EX",self.ex)
        print("EM",self.em)
        print("EN",self.en)
        print("JW",self.jw)
        print("JSP",self.jsp)
        print('*'*10)

    def classify_file(self,name):
        
        #print('In Classify')
        ###
        pks_pattern="[0-9a-z,_]+.pks"
        sql_pattern="[0-9a-z,_]+.sql"
        ###
        bj_pattern="[0-9a-z,_]+_bj_[0-9a-z,_]+.pkb"
        cl_pattern="[0-9a-z,_]+_cl_[0-9a-z,_]+.pkb"
        el_pattern="[0-9a-z,_]+_el_[0-9a-z,_]+.pkb"
        ew_pattern="[0-9a-z,_]+_ew_[0-9a-z,_]+.pkb"
        ex_pattern="[0-9a-z,_]+_ex_[0-9a-z,_]+.pkb"
        em_pattern="[0-9a-z,_]+_em_[0-9a-z,_]+.pkb"
        en_pattern="[0-9a-z,_]+_en_[0-9a-z,_]+.pkb"
        jw_pattern="[0-9a-z,_]+_jw_[0-9a-z,_]+.pkb"
        jsp_pattern="[0-9a-z,_]+.jsp"
        ###            
                
        if re.search(pks_pattern,name):
            print("pks found a match")
        elif re.search(sql_pattern,name):
            print("sql found a match")
        else:
            if re.search(bj_pattern,name):
                self.bj=self.bj+1
                #print("bj found a match")
            if re.search(cl_pattern,name):
                self.cl=self.cl+1
                #print("bj found a match")
            if re.search(el_pattern,name):
                self.el=self.el+1
                #print("bj found a match")
            if re.search(ew_pattern,name):
                self.ew=self.ew+1
                #print("bj found a match")
            if re.search(ex_pattern,name):
                self.ex=self.ex+1
                #print("bj found a match")
            if re.search(em_pattern,name):
                self.em=self.em+1
                #print("bj found a match")
            if re.search(en_pattern,name):
                self.en=self.en+1
                #print("bj found a match")
            if re.search(jw_pattern,name):
                self.jw=self.jw+1
                #print("bj found a match")
            if re.search(jsp_pattern,name):
                self.jsp=self.jsp+1
                #print("bj found a match")




def main():
    pkg_path=os.sys.argv[1]
    root_dir=dir("root",pkg_path)
    root_dir.do_something()
    
    


if __name__ == "__main__":
    main()