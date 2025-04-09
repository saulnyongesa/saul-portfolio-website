from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import *
from api.serializers import *

@api_view(['GET'])
def get_user(request, user_id):
    """
    Retrieve a user by ID.
    """
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
# Projects=========================================================================================
@api_view(['GET'])
def get_projects(request):
    """
    Retrieve all projects.
    """
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_project(request):
    """
    Create a new project.
    """
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_project(request, project_id):
    """
    Retrieve a specific project by ID.
    """
    try:
        project = Project.objects.get(id=project_id)
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_project(request, project_id):
    """
    Update an existing project.
    """
    try:
        project = Project.objects.get(id=project_id)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_project(request, project_id):
    """
    Delete a project.
    """
    try:
        project = Project.objects.get(id=project_id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Project End ======================================================================================

# Skills=========================================================================================

@api_view(['GET'])
def get_skills(request):
    """
    Retrieve all skills.
    """
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_skill(request):
    """
    Create a new skill.
    """
    serializer = SkillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_skill(request, skill_id):
    """
    Retrieve a specific skill by ID.
    """
    try:
        skill = Skill.objects.get(id=skill_id)
        serializer = SkillSerializer(skill, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['PUT'])
def update_skill(request, skill_id):
    """
    Update an existing skill.
    """
    try:
        skill = Skill.objects.get(id=skill_id)
        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_skill(request, skill_id):
    """
    Delete a skill.
    """
    try:
        skill = Skill.objects.get(id=skill_id)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
# Skills End =====================================================================================

# Emails=========================================================================================
@api_view(['GET'])
def get_emails(request):
    """
    Retrieve all emails.
    """
    emails = Email.objects.all()
    serializer = EmailSerializer(emails, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['POST'])
def create_email(request):
    """
    Create a new email.
    """
    serializer = EmailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_email(request, email_id):
    """
    Retrieve a specific email by ID.
    """
    try:
        email = Email.objects.get(id=email_id)
        serializer = EmailSerializer(email, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Email.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_email(request, email_id):
    """
    Delete an email.
    """
    try:
        email = Email.objects.get(id=email_id)
        email.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Email.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
# Email End =====================================================================================

