from django import forms

class CandidateDataForm(forms.Form):

    category_choices_list = [
        ('SM', 'State Merit (SM)'), ('EZ', 'Ezhava (EZ)'),
        ('MU', 'Muslim (MU)'), ('BH', 'Other Backward Hindu (BH)'),
        ('LA', 'Latin Catholic & Anglo Indian (LA)'), ('DV', 'Dheevara & Related (DV)'),
        ('VK', 'Viswakarma & Related (VK)'), ('BX', 'Other Backward Christian (BX)'),
        ('KU', 'Kudumbi (KU)'), ('KN', 'Kusavan & Related (KN)'),
        ('SC', 'Scheduled Caste (SC)'), ('ST', 'Scheduled Tribe (ST)')
    ]

    course_choice_list = [
        ('Computer Science & Engineering', 'Computer Science & Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electical & Electronics Engineering', 'Electical & Electronics Engineering'),
        ('B.Pharm', 'B.Pharm'), ('Architecture', 'Architecture'), ('Electronics & Communication Engineering', 'Electronics & Communication Engineering'), ('Information Technology', 'Information Technology'), ('Applied Electonics & Instrumentation', 'Applied Electonics & Instrumentation'),
        ('Food Technology', 'Food Technology'), ('Robotics & Automation', 'Robotics & Automation'), ('Aeronautical Engineering', 'Aeronautical Engineering'), ('Mechatronics Engineering', 'Mechatronics Engineering'), ('Automobile Engineering', 'Automobile Engineering'),
        ('Aritificial Intelligence and Data Science', 'Aritificial Intelligence and Data Science'), ('Dairy Technology', 'Dairy Technology'), ('Electronics & Instrumentation', 'Electronics & Instrumentation'), ('Bio Technology and Biomechanical Engg', 'Bio Technology and Biomechanical Engg'),
        ('Mechanical Engg. (Automobile)', 'Mechanical Engg. (Automobile)'), ('Bio Medical Engineering', 'Bio Medical Engineering'), ('Mechanical (Production Engg.)', 'Mechanical (Production Engg.)'), ('Instrumentation & Control Engg', 'Instrumentation & Control Engg'),
        ('Naval Arch. & Ship Building', 'Naval Arch. & Ship Building'), ('Safety & Fire Engineering', 'Safety & Fire Engineering'), ('Computer Science & Engineering (Aritificial Engineering)','Computer Science & Engineering (Aritificial Engineering)'), ('Computer Science & Engg. (Artificial Intelligence & Machine Learning)', 'Computer Science & Engg. (Artificial Intelligence & Machine Learning)'),
        ('Bio Technology', 'Bio Technology'), ('Industrial Engineering', 'Industrial Engineering'), ('Electronics & Biomedical Engineering', 'Electronics & Biomedical Engineering'), ('Computer Science & Engineering (Cyber Security)', 'Computer Science & Engineering (Cyber Security)'), ('Computer Science & Enggineering (Data Science)', 'Computer Science & Enggineering (Data Science)'),
        ('Metallurgical and Materials Engineering', 'Metallurgical and Materials Engineering'), ('Agricultural Engineering', 'Agricultural Engineering'), ('Polymer Engineering', 'Polymer Engineering'), ('Printing Technology', 'Printing Technology'), ('Production Engineering', 'Production Engineering'),
        ('Artificial Intelligence', 'Artificial Intelligence'), ('Electrical & Computer Engineering', 'Electrical & Computer Engineering')
    ]

    category = forms.ChoiceField(choices=sorted(category_choices_list), required=True)
    course = forms.ChoiceField(choices=sorted(course_choice_list), required=True)
    rank = forms.IntegerField(required=True)