from django.test import TestCase

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self)
        ''' 
        creating a new user and saving it
        '''
        self.new_user = User(password='brownsugar',  email = "bs@gmail.com",password = "bswopqd")
        self.new_user.save()

        '''
        creating a new profile and saving it
        '''
        self.new_profile = Profile(profile_photo='photo.jpg', bio='Nice')
        self.new_profile.save()

        '''
        creating a new image and saving it
        '''
        self.new_image = Image(image='image.jpg', img_name='house',caption='old house', likes=1, comments='i like it', profile=self.new_profile)
        self.new_image.save()

    def tearDown(self) -> None:
        Image.objects.all().delete()
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_instance(self):
        '''
        This will test whether the new image created is an instance of the Image class
        '''
        self.assertTrue(isinstance(self.new_image, Image))
        self.assertTrue(isinstance(self.new_profile, Profile))
        self.assertTrue(isinstance(self.new_user, User))

    def test_save_image_method(self):
        '''
        Tests whether new image is added
        '''
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        '''
        Tests whether new image is deleted
        '''
        self.new_image.save_image()
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_caption(self):
        '''
        Tests whether the image is updated
        '''
        self.new_image.save_image()
        updated_caption = Image.update_caption(self.new_image.id, 'old house')
        self.assertEqual(updated_caption.image_caption, 'old house')


    def test_get_image_by_profile(self):
        '''
        This tests whether images for profiles are retrieved
        '''
        self.new_image.save_image
        self.new_user.save()
        profile_image = Image.get_images(self.new_user)
        self.assertEqual(len(profile_image),1 )

    
class ProfileTestClass(TestCase):

    def setUp(self) 
        self.new_profile = Profile(profile_photo='photo.jpg', bio='Nice')

    def tearDown(self)
        Profile.objects.all().delete()

    def test_save_user_profile(self):
        self.new_profile.save_user_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_user_profile(self):
        self.new_profile.save_user_profile()
        self.new_profile.delete_user_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_profile_bio(self):
        self.new_profile.save_user_profile()
        updated_profile = Profile.update_profile_bio(self.new_profile.id, 'Bad')
        self.assertEqual(updated_profile.bio, 'Bad')

    def test_update_profile_pic(self):
        self.new_profile.save_user_profile()
        updated_profile = Profile.update_profile_pic(self.new_profile.id, 'gp.jpg')
        self.assertTrue(updated_profile.profile_pic != self.new_profile.profile_pic)


class CommentTestClas(TestCase):
    '''
    Class that tests the images
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.new_image = Image(image='image.jpg', img_name='house',caption='old house', likes=1, comments='i like it', profile=self.new_profile)
        self.new_profile = Profile(profile_photo='photo.jpg', bio='Nice')
        self.comment = Comment(image=self.new_image, content= 'Throwback', user = self.new_profile)

        self.new_profile.save()
        self.new_image.save_image()
        self.comment.save_comment()

    def tearDown(self):
        '''
        Clears data after test
        '''
        Image.objects.all().delete()
        Comment.objects.all().delete()

    def test_comment_instance(self):
        '''
        Tests whether the new comment created is an instance of Comment class
        '''
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment_method(self):
        '''
        Tests whether new comment is added 
        '''
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)> 0)

    def test_delete_comment(self):
        '''
        Tests whether comment is deleted
        '''
        self.comment.save_comment()
        comments1 = Comment.objects.all()
        self.assertEqual(len(comments1),1)
        self.comment.delete_comment()
        comments2 = Comment.objects.all()
        self.assertEqual(len(comments2),0)

    def test_get_image_comments(self):
        '''
        Tests whether comments can be retrieved by image
        '''
        comments = Comment.get_image_comment(self.new_image)
        self.assertTrue(len(comments) > 0)
    

