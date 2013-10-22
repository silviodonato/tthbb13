#ifndef DaqSource_DaqFakeReader_h
#define DaqSource_DaqFakeReader_h

/** \class DaqFakeReader
 *  Generates empty FEDRawData of random size for all FEDs
 *  Proper headers and trailers are included; but the payloads are all 0s
 *  \author N. Amapane - CERN
 */

#include "EvffedFillerRB.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "DataFormats/Provenance/interface/EventID.h"
#include "DataFormats/FEDRawData/interface/FEDRawDataCollection.h"
#include <algorithm>



class DaqFakeReader : public edm::EDProducer
{
 public:
  //
  // construction/destruction
  //
  DaqFakeReader(const edm::ParameterSet& pset);
  virtual ~DaqFakeReader();
  

  //
  // public member functions
  //

  // Generate and fill FED raw data for a full event
  virtual int fillRawData(edm::Event& e,
			  FEDRawDataCollection*& data);

  virtual void produce(edm::Event&, edm::EventSetup const&);
  
private:
  //
  // private member functions
  //
  void fillFEDs(const int, const int,
		edm::EventID& eID,
		FEDRawDataCollection& data,
		float meansize,
		float width);
  void fillFED1023(edm::EventID& eID,
		   FEDRawDataCollection& data);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const& iL, edm::EventSetup const& iE);
 private:
  //
  // member data
  //
  edm::RunNumber_t    runNum;
  edm::EventNumber_t  eventNum;
  bool                empty_events;
  unsigned int        meansize; // in bytes
  unsigned int        width;
  unsigned int        injected_errors_per_million_events;
  unsigned int        modulo_error_events;
  evf::EvffedFillerRB frb;
};

#endif
