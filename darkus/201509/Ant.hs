module Ant where

import Test.QuickCheck

data Ant = K | L | P | H
  deriving (Eq, Read, Show)

type AntList = [Ant]

instance Arbitrary Ant where
  arbitrary = elements [K, L, P, H]

change_price :: Ant -> Ant -> Ant -> Ant -> Int
-- Syn
change_price K L K H = 0
change_price L K L P = 0
change_price L L L H = 0
change_price P K P P = 0
change_price K H K L = 0
change_price L P L K = 0
change_price L H L L = 0
change_price P P P K = 0
-- Weak
change_price H K H L = 5
change_price P K K P = 5
change_price P P K P = 5
change_price K K L L = 5
change_price K K L H = 5
change_price H L H K = 5
change_price K P P K = 5
change_price K P P P = 5
change_price L L K K = 5
change_price L H K K = 5
-- Strong
change_price P L P H = 25
change_price P L K L = 25
change_price P L K H = 25
change_price P H K L = 25
change_price P H K H = 25
change_price H P P H = 25
change_price H P P L = 25
change_price H P K L = 25
change_price H P K H = 25
change_price P H P L = 25
change_price K L P L = 25
change_price K H P L = 25
change_price K L P H = 25
change_price K H P H = 25
change_price P H H P = 25
change_price P L H P = 25
change_price K L H P = 25
change_price K H H P = 25
-- Other
change_price _ _ _ _ = 100

