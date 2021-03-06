import os
from django.utils.timezone import now
from blog.models import Blog
from blog.helper import update

def create_obj(name, file_content, is_proj):
    obj = Blog()
    # create file with name
    obj.title = name;
    # and save the contets
    obj.content = file_content
    obj.pub_date = now()
    obj.is_project = is_proj
    obj.save()

def update_obj(obj, new_content):
    obj.content = new_content
    obj.save()

# chdir into either project or blogs
# project is true if the dir is the proj dir
def check_files(project):
    files = os.listdir(os.curdir)
    curr_dur = os.path.abspath(os.curdir)
    for f in files:
        print("file name {}", f)
        if os.path.isdir(f):
            raise Exception("There shouldn't be any folders where the markdown files are stored")
        elif "draft" not in f and ".md" in f:
            content = ""
            dir = os.path.join(curr_dur, f)
            md_title = strip_file_type(f)
            with open(dir) as file:
                content = file.read()

            if Blog.objects.filter(title=md_title):
                update_obj(Blog.objects.get(title=md_title), content)
            else:
                create_obj(md_title, content, project)


        # do nothing for everything else

def strip_file_type(file_name):
    if len(file_name) < 4:
        raise Exception("File name too short should be more than 3 characters")
    return file_name[:len(file_name)-3]

def update():
    abs_pth = os.path.abspath(os.curdir)
    content_path = os.path.join(abs_pth, "content")
    print(content_path)

    # chdir needs the full path name for whatever reason
    # changing to prorojects
    os.chdir(os.path.join(content_path, "projects"))
    check_files(True)
    os.chdir(os.path.join(content_path, "blogs"))
    check_files(False)
