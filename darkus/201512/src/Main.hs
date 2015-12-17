{-# LANGUAGE OverloadedStrings #-}

module Main where

import Mutation (parseData, MDataT(..), mdata2normals)
import Matrix (MatrixT(..), matrices)
import Stats (pValue, sigma)

import Data.Text (append, Text, unpack)
import Text.Printf (printf, hPrintf)
import System.IO (withFile, IOMode(..))
import Control.Monad (forM_)

mdata2Ints :: MDataT -> [Integer]
mdata2Ints (MData _ a b c d) = map (\x -> x :: Integer) [a, b, c, d]

toTuple :: [a] -> (a, a, a, a)
toTuple xs@(a:b:c:d:[]) = (a,b,c,d)

mdataPValue :: MDataT -> Double
mdataPValue = pValue . toTuple . mdata2Ints

readInfo :: FilePath -> IO [MDataT]
readInfo filepath = do
  content <- readFile filepath
  return $ parseData content

showMData :: MDataT -> String
showMData (MData prop a b c d) = unwords [(unpack prop) ++ ":", pretty_pvalue]
  where pretty_pvalue = printf "%.5f" pvalue
        pvalue = pValue (a, b, c, d)

showMDataCor :: MDataT -> String
showMDataCor mdata = unwords [(unpack $ mname mdata) ++ ":", pretty_cor]
  where pretty_cor = case withMutation mdata of
                     Just True -> "T"
                     Just False -> "F"

-- showMDataCor (MData prop a b c d) = unwords [(unpack prop) ++ ":", pretty_cor]
--   where pretty

withMutation :: MDataT -> Maybe Bool
withMutation mdata
      | correspondence == [1.0, 0.0] = Just True
      | correspondence == [0.0, 1.0] = Just False
      | otherwise                    = Nothing
  where correspondence = drop 2 corresp_matrix
        corresp_matrix = snd $ minimum $ map sigma_matrix matrices
        sigma_matrix (Matrix xs) = ((sigma normal_mdata xs), xs)
        normal_mdata = mdata2normals mdata

mutationFilter m = case withMutation m of
                   Nothing -> False
                   Just x -> True

main :: IO()
main = do
  info <- readInfo "data.txt"

  let significants = filter ((<0.05) . mdataPValue) info
  withFile "Result_01.txt" WriteMode $ \h -> do
    forM_ significants (\m -> hPrintf h "%s\n" $ showMData m)

  let mutational = filter mutationFilter significants
  withFile "Result_02.txt" WriteMode $ \h -> do
    forM_ mutational (\m -> hPrintf h "%s\n" $ showMDataCor m)

  -- let input = unlines ["a: 158 70 15 22", "b: 34 34 34 34", "cc: 1 1 1 1", "dddd: a 3 23 4" ]
  -- mapM_ putStrLn $ map (\x -> concat [show x, ":", show $ mdataPValue x]) (parseData input)
  -- putStrLn "This is main function"
