#ifndef NET
#define NET

#include <string.h>
#include <omnetpp.h>
#include <packet_m.h>

using namespace omnetpp;

class Net: public cSimpleModule {
private:
    cOutVector hopCount;
public:
    Net();
    virtual ~Net();
protected:
    virtual void initialize();
    virtual void finish();
    virtual void handleMessage(cMessage *msg);
};

Define_Module(Net);

#endif /* NET */

Net::Net() {
}

Net::~Net() {
}

void Net::initialize() {
    hopCount.setName("hopCount");
}

void Net::finish() {
}

void Net::handleMessage(cMessage *msg) {

    // All msg (events) on net are packets
    Packet *pkt = (Packet *) msg;

    // If this node is the final destination, send to App
    if (pkt->getDestination() == this->getParentModule()->getIndex()) {
        send(msg, "toApp$o");
        hopCount.record(pkt->getHopCount());
    }
    else{
        pkt->setHopCount(pkt->getHopCount() + 1);
        // Si el paquete viene de izquieda, sale por derecha:
        if(pkt->arrivedOn("toLnk$i",1)){
            send(msg, "toLnk$o", 0);
        }
        // Si el paquete viene de derecha sale por izquirda:
        else if(pkt->arrivedOn("toLnk$i",0)){
            send(msg, "toLnk$o", 1);
        }
        // Cuando no viene de ningun lado, es creado por nosotros, 
        // entonces que se envie alguna direccion al azar:
        else{
            send(msg, "toLnk$o", rand() % 2);
        }
    }
}
