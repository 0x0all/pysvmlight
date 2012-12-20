# Bismillahi-r-Rahmani-r-Rahim

import unittest

from svmlight import Learner, DocumentFactory, SupportVector

class LearnerTestCase(unittest.TestCase):
    def testConstruction(self):
        self.assertEqual(str(Learner()),
                         "Learner(biased_hyperplane=True)")

    def testSetBiasedHyperplane(self):
        l = Learner()
        l.biased_hyperplane = False
        self.assertEqual(str(l), "Learner(biased_hyperplane=False)")

    def testLearn(self):
        f = DocumentFactory()
        docs = [f.new(x.split()) for x in [
                "this is a nice long document",
                "this is another nice long document",
                "this is rather a short document",
                "a horrible document",
                "another horrible document"]]
        print docs
        l = Learner()
        model = l.learn(docs, [1, 1, 1, -1, -1])
        print model, model.bias
        self.assertEqual(5, model.num_docs)
        self.assertEqual(10, len(model.plane))
        self.assertNotEqual(model.bias, 0)
        print model.plane
    
    def testLearnUnbiased(self):
        f = DocumentFactory()
        docs = [f.new(x.split()) for x in [
                "this is a nice long document",
                "this is another nice long document",
                "this is rather a short document",
                "a horrible document",
                "another horrible document"]]
        print docs
        l = Learner()
        l.biased_hyperplane = False
        model = l.learn(docs, [1, 1, 1, -1, -1])
        print model, model.bias
        self.assertEqual(5, model.num_docs)
        self.assertEqual(10, len(model.plane))
        self.assertEqual(model.bias, 0)
        print model.plane
    
if __name__ == '__main__':
    unittest.main()
