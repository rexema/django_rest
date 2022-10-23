import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from users.models import CustomUser
from .models import Project, ToDo


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        email = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root,info, **kwargs):
        user = CustomUser.objects.get(id=kwargs.get('id'))
        user.email = kwargs.get('email')
        user.save()
        return cls(user=user)


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = CustomUser.objects.create(**kwargs)
        user.save()
        return cls(user=user)


class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.List(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        CustomUser.objects.get(id=kwargs.get('id')).delete()
        return cls(user=CustomUser.objects.all())


class Mutations(ObjectType):
    update_user = UserUpdateMutation.Field()
    create_user = UserCreateMutation.Field()
    delete_user = UserDeleteMutation.Field()


class Query(ObjectType):

    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(ToDoType)

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    user_by_id = graphene.Field(UserType, id=graphene.Int(required=False))

    def resolve_user_by_id(root, info, id=None):
        if id:
            return CustomUser.objects.get(id=id)

        return CustomUser.objects.all()

    project_by_user = graphene.List(ProjectType, username=graphene.String(required=False))

    def resolve_project_by_user(root, info, username=None):
        projects = Project.objects.all()
        if username:
            return projects.filter(user__username=username)
        return projects

    todo_by_project = graphene.List(ToDoType, name=graphene.String(required=False))

    def resolve_todo_by_project(root, info, name=None):
        if name:
            return ToDo.objects.filter(project__name=name)

        return ToDo.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutations)
