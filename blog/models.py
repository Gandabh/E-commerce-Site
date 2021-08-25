from django.db import models
from product.models import Category
from account.models import User



class Tag(models.Model):
    """
    this model saves tags
    """
    tag_name = models.CharField('Tag name', max_length=50)

    # moderation's
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
            verbose_name = 'Tag'
            verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag_name



class Post(models.Model):
    """
    this model saves posts
    """
    image=models.ImageField("Shekli daxil edin",null=True,blank=True,upload_to='blog_images')
    title = models.CharField('Basliq', max_length=40)
    user=models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name="posts")
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, db_index=True, related_name="posts")
    tag=models.ManyToManyField(Tag)
    slug = models.CharField('Slug', editable=False, max_length=250)

    # moderation's
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
            verbose_name = 'Post'
            verbose_name_plural = 'Posts'

    def __str__(self):
            return self.title




class Comment(models.Model):
    """
    this model saves Comments
    """
    user=models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name="comments")
    comment=models.TextField('Şərh', null=True, blank=True)
    blog=models.ForeignKey(Post, on_delete=models.CASCADE, db_index=True, related_name="comments")
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True, related_name='replies')


    # moderation's
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Comment'
            verbose_name_plural = 'Comments'


    def __str__(self):
        return self.user.username