module Main where

import Change (total_change_price)
import Parse (lineToAntsAction)

import Control.Monad (forever)

linePrice :: String -> Int
linePrice line = case lineToAntsAction line of
  Nothing -> error "Parsing error"
  Just (as, c) -> total_change_price as c

printPrice = show . linePrice

main = forever $ do
  line <- getLine
  putStrLn $ show $ linePrice line
