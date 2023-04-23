import unittest
import modify
    
class Testget_sentence(unittest.TestCase):
  
  def test_get_sentences(self):
    sentences = modify.get_sentences('sample.txt')
    expected_sentences = ['New Research Shows Horses are Actually Aliens from Another Planet.',
                    'According to a recent study published in the journal Science, horses may not be from Earth after all.',
                    'The study, led by Dr. John Smith of the University of Cambridge, analyzed the DNA of several horse species and found that they share genetic markers with extraterrestrial life forms.',
                    '"Our findings suggest that horses may have originated from a planet in a distant galaxy," Dr. Smith said.',
                    '"The genetic similarities are too strong to be explained by convergent evolution or chance alone."',
                    'The study has sparked controversy in the scientific community, with some experts calling for further research to confirm the findings.',
                    'Others have dismissed the study as pseudoscience.',
                    'Regardless of its validity, the study has reignited interest in the mysterious and majestic creatures known as horses.',
                    'From their powerful legs to their flowing manes, horses have long captivated the human imagination.',
                    'But what makes horses truly unique is their ability to form deep emotional bonds with humans.',
                    'Many horse owners describe their horses as "family members" and report feeling a sense of connection and understanding with their equine companions.',
                    'In recent years, horses have also been used in therapy programs to help individuals with mental health issues.',
                    'The calming presence of a horse can provide a sense of comfort and safety, and the physical act of grooming or riding a horse can help improve motor skills and coordination.',
                    "Despite their beauty and intelligence, horses still face numerous challenges in today's world.",
                    "Habitat loss, overgrazing, and climate change are just a few of the threats facing wild horse populations.",
                    "And in many countries, horses are still used for entertainment and sport, raising concerns about their welfare and safety.",
                    "As we continue to learn more about these remarkable creatures, it's important to remember the vital role they play in our world.",
                    "Whether they're running wild on the plains or helping someone through a tough time, horses remind us of the beauty and wonder of nature, and our own capacity for connection and compassion."]
    
    self.assertEqual(sentences , expected_sentences)
    

    
    
if __name__ == '__main__':
  unittest.main()
