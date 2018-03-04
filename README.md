# gifPrinterzClient

## Gif Printer Client ran by django using python3.6

### Dependecies 

yum: 
- "@development"
- "python36u"
- "python36u-pip"
- "git"
- "nginx"

pip:
- gunicorn
- Pillow
- django

## HINTS

You will need to add to the playbook that is already in the ansible directory. Add tasks to do the following:

- install dependecies for yum and pip (http://docs.ansible.com/ansible/latest/yum_module.html) (http://docs.ansible.com/ansible/latest/pip_module.html)
- copy your ssh deployment key for your fork (http://docs.ansible.com/ansible/latest/copy_module.html)
- clone your for using the ssh url (http://docs.ansible.com/ansible/latest/git_module.html)
