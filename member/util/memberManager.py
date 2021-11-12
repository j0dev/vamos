from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):     # 콘솔 유저 생성 프로세스 (슈퍼어드민 등)
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.is_active = True   # 인증 로직 개발 예정
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email,
            username,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.is_agreement = True
        user.is_staff = True
        user.save(using=self._db)
        return user