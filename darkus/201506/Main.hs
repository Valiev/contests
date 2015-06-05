module Main where

import Data.List (sort, reverse)

type CountryName = String
type Bugs = Int
data Country = Country {
                  name :: CountryName,
                  bugs :: Bugs
               } deriving (Show, Eq)

instance Ord Country where
  (Country _ b1) `compare` (Country _ b2) = b1 `compare` b2

updateCountries :: [Country] -> CountryName -> [Country]
updateCountries [] country_name     = [Country country_name 1]
updateCountries (x:xs) country_name = if name' == country_name
                                      then x':xs
                                      else x:(updateCountries xs country_name)
                                where x' = Country name' num'
                                      name' = name x
                                      num' = 1 + bugs x

multipleUpdateCountries :: [Country] -> [CountryName] -> [Country]
multipleUpdateCountries cs [] = cs
multipleUpdateCountries cs (x:xs) = multipleUpdateCountries cs' xs
  where cs' = updateCountries cs x


popularCountries :: Int -> [Country] -> [Country]
popularCountries n cs = take n $ (reverse . sort) cs

main = do
  undefined
