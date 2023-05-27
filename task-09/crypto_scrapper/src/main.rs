use csv::Writer;
use std::error::Error;
use scraper::Selector;

fn main() -> Result<(), Box<dyn Error>> {
    let response = reqwest::blocking::get(
        "https://crypto.com/price",
    )
    .unwrap()
    .text()
    .unwrap();

    let document = scraper::Html::parse_document(&response);

    let name_selector = Selector::parse(".css-ttxvk0 > p").unwrap();
    let price_selector = Selector::parse(".css-b1ilzc").unwrap();
    let change24_selector = Selector::parse("td.css-1b7j986 > p").unwrap();
    let volume24_selector = Selector::parse("td.css-1nh9lk8").unwrap();
    let marketcap_selector= scraper::Selector::parse(".css-1nh9lk8+.css-1nh9lk8").unwrap();
    
    let names = document.select(&name_selector).map(|x| x.inner_html());
    let prices = document.select(&price_selector).map(|x| x.inner_html());
    let changes24 = document.select(&change24_selector).map(|x| x.inner_html());
    let volumes24 = document.select(&volume24_selector).map(|x| x.inner_html());
    let market_cap = document.select(&marketcap_selector).map(|x| x.inner_html());


    let mut writer = Writer::from_path("output.csv")?;
    
    writer.write_record(&["NAME", "PRICE", "24H CHANGE", "24H VOLUME", "MARKET CAP"])?;

    for ((((name, price), change), volume), marketcap) in names.zip(prices).zip(changes24).zip(volumes24).zip(market_cap) {
        writer.write_record(&[name, price, change, volume, marketcap])?;
    }

    writer.flush()?;

    Ok(())
}