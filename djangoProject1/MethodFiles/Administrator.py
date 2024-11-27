# file for Admin methods
from djangoProject1.MethodFiles.Interfaces import CreateCourseInterface, CreateLabInterface, CheckPermissionInterface, \
    EditUserInterface
from djangoProject1.models import Course, User

class CreateCourse(CreateCourseInterface):
    @staticmethod
    def create_course(name, instructor):
        #if name or instructor are the wrong type return None
        if not isinstance(instructor, User) or not isinstance(name, str):
            return None

        #if any of the inputs are none then return None
        if name == None or name == "" or instructor == None:
            return None

        #if the role isn't instructor then we can't assign to a course so we return None
        if instructor.role != "Instructor":
            return None

        #if the course already exists then return None
        if Course.objects.filter(name=name).exists():
            return None


        #if everything is fine then we can create the course no problem
        course = Course(name=name)
        course.save()
        course.instructors.add(instructor)

        return course

class CreateLab(CreateLabInterface):
    @staticmethod
    def create_lab(name, instructor):
        pass

class CheckPermission(CheckPermissionInterface):
    @staticmethod
    def check_admin(user):
        pass

    @staticmethod
    def check_instructor(self, user):
        pass

class EditUser(EditUserInterface):
    @staticmethod
    def edit_user(self, user):
        pass