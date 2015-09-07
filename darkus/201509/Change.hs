module Change where

import Ant (Ant(..), AntList, change_price)
import Test.QuickCheck

type Pos = Int
data Change = Delete Pos | Paste Pos Ant | Change Pos Ant
                deriving Show

applyRawChange :: AntList -> Change -> AntList
applyRawChange as c = case c of
    Delete n -> deleteChange as n
    Paste n a -> pasteChange as n a
    Change n a -> changeChange as n a

deleteChange :: [a] -> Pos -> [a]
deleteChange as n = start ++ end
  where start = take (n-1) as
        end = drop n as

changeChange :: [a] -> Pos -> a -> [a]
changeChange as n a = start ++ [a] ++ end
  where start = take (n-1) as
        end = drop n as

pasteChange :: [a] -> Pos -> a -> [a]
pasteChange as n a = start ++ [a] ++ end
  where start = take n as
        end = drop n as

apply :: AntList -> Change -> AntList
apply ants c = adjust result
  where result = applyRawChange ants c

adjust :: AntList -> AntList
adjust [] = [H, H]
adjust [x] = case x of
  H -> [H, H]
  otherwise -> [x, H, H, H]
adjust (x:y:zs) = x:y:(adjust zs)

prop_adjust :: AntList -> Bool
prop_adjust xs = (take 2 $ reverse $ adjust xs) == [H, H]

pairs :: [a] -> [a] -> [(a, a)]
pairs xs [] = zip xs xs
pairs [] ys = zip ys ys
pairs (x:xs) (y:ys) = (x,y):(pairs xs ys)

enlarge :: [a] -> [a] -> ([a], [a])
enlarge x y = unzip $ pairs x y

total_change_price :: AntList -> Change -> Int
total_change_price as c = sum changes
  where changes = helper' before after
        before' = adjust as
        after' = adjust $ apply as c
        (before, after) = enlarge before' after'
        helper' :: AntList -> AntList -> [Int]
        helper' [] [] = []
        helper' (x:y:zs) (x':y':zs') = (change_price x y x' y'):(helper' zs zs')
